import os
import re
import sys
import time
import urllib.request
import json
from datetime import datetime

# Configuration
SUBDOMAIN = "parlonsdesign"
OUTPUT_DIR = "./raw/sources"
MAX_EPISODES = 100

os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(name):
    # Remplacer les caractères non autorisés
    clean_name = re.sub(r'[\\/*?:"<>|#]', "", name)
    clean_name = clean_name.replace(" ", "_").replace("'", "_").replace('"', "_")
    clean_name = re.sub(r'_+', '_', clean_name)
    return clean_name.strip('_')

def get_headers():
    return {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

def fetch_json(url):
    req = urllib.request.Request(url, headers=get_headers())
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Erreur lors de la requête sur {url} : {e}")
        return None

def main():
    print(f"=== DÉBUT DE LA RÉCUPÉRATION DEPUIS SUBSTACK (Objectif: {MAX_EPISODES} épisodes) ===")
    
    episodes_fetched = 0
    offset = 0
    limit = 50
    
    all_episodes = []
    
    # 1. Récupérer la liste des articles
    while len(all_episodes) < MAX_EPISODES:
        url = f"https://{SUBDOMAIN}.substack.com/api/v1/posts?sort=new&limit={limit}&offset={offset}"
        print(f"Récupération de la liste des posts (offset={offset}, limit={limit})...")
        posts = fetch_json(url)
        
        if not posts:
            print("Impossible de récupérer d'autres posts ou fin de la liste atteinte.")
            break
            
        all_episodes.extend(posts)
        print(f" -> {len(posts)} posts trouvés. Total accumulé : {len(all_episodes)}")
        
        if len(posts) < limit:
            # Plus de posts disponibles
            break
            
        offset += limit
        time.sleep(1) # Petit délai
        
    all_episodes = all_episodes[:MAX_EPISODES]
    print(f"\nTotal d'épisodes à traiter : {len(all_episodes)}")
    
    success_count = 0
    skipped_count = 0
    failed_count = 0
    
    # 2. Récupérer les transcriptions pour chaque épisode
    for idx, post in enumerate(all_episodes, start=1):
        title = post.get('title')
        slug = post.get('slug')
        post_date_raw = post.get('post_date', '')
        
        # Formater la date en AAAA-MM-JJ
        try:
            # post_date est généralement sous format ISO 2026-05-07T22:40:01Z
            date_str = datetime.strptime(post_date_raw[:10], "%Y-%m-%d").strftime("%Y-%m-%d")
        except Exception:
            date_str = "Date inconnue"
            
        filename = f"{date_str}_{sanitize_filename(title)}.md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if os.path.exists(filepath):
            print(f"[{idx}/{len(all_episodes)}] Déjà récupéré : {title}")
            success_count += 1
            continue
            
        print(f"[{idx}/{len(all_episodes)}] Traitement : {title}...")
        
        # Récupérer les détails complets de l'article via l'API post détaillée
        post_url = f"https://{SUBDOMAIN}.substack.com/api/v1/posts/{slug}"
        post_details = fetch_json(post_url)
        
        if not post_details:
            print(f" -> Échec de la récupération des détails pour {title}")
            failed_count += 1
            time.sleep(1)
            continue
            
        podcast_upload = post_details.get('podcastUpload')
        if not podcast_upload:
            print(f" -> Ce post n'est pas un podcast ou n'a pas d'audio uploadé.")
            skipped_count += 1
            time.sleep(0.5)
            continue
            
        transcription = podcast_upload.get('transcription', {})
        cdn_url = transcription.get('cdn_url')
        
        if not cdn_url:
            print(f" -> Aucune transcription disponible sur Substack pour cet épisode.")
            skipped_count += 1
            time.sleep(0.5)
            continue
            
        # Récupérer le fichier JSON de transcription
        print(f"   -> Téléchargement de la transcription...")
        trans_data = fetch_json(cdn_url)
        
        if not trans_data or not isinstance(trans_data, list):
            print(f"   -> Échec du décodage de la transcription JSON.")
            failed_count += 1
            time.sleep(1)
            continue
            
        # Formater la transcription
        formatted_paragraphs = []
        current_speaker = None
        current_paragraph = []
        
        for entry in trans_data:
            text = entry.get('text', '').strip()
            speaker = entry.get('speaker', 'SPEAKER')
            
            if not text:
                continue
                
            if speaker != current_speaker:
                if current_paragraph:
                    formatted_paragraphs.append(f"**{current_speaker}** : {' '.join(current_paragraph)}")
                current_speaker = speaker
                current_paragraph = [text]
            else:
                current_paragraph.append(text)
                
        if current_paragraph:
            formatted_paragraphs.append(f"**{current_speaker}** : {' '.join(current_paragraph)}")
            
        full_transcript_text = "\n\n".join(formatted_paragraphs)
        
        # Sauvegarder sous format Markdown
        escaped_title = title.replace('&', '&amp;').replace('"', '\\"')
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\n")
            f.write(f"title: \"{escaped_title}\"\n")
            f.write(f"date: \"{date_str}\"\n")
            f.write(f"youtube_url: \"\"\n") # On garde la clé vide ou à compléter
            f.write(f"substack_url: \"https://{SUBDOMAIN}.substack.com/p/{slug}\"\n")
            f.write(f"type: podcast\n")
            f.write(f"---\n\n")
            f.write(full_transcript_text)
            
        print(f"   -> Enregistré avec succès ! ({len(trans_data)} segments)")
        success_count += 1
        time.sleep(1.5) # Respect des limites de requêtes
        
    print(f"\n=== FIN DE LA RÉCUPÉRATION ===")
    print(f"Succès : {success_count} | Ignorés : {skipped_count} | Échecs : {failed_count}")

if __name__ == "__main__":
    main()
