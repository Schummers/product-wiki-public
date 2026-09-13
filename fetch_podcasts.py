import os
import re
import sys
from datetime import datetime
import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi

# Configuration
CHANNEL_URL = "https://www.youtube.com/@ParlonsDesign/videos"
OUTPUT_DIR = "./raw/sources"
MAX_EPISODES = 100

os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(name):
    # Remplacer les caractères non autorisés
    clean_name = re.sub(r'[\\/*?:"<>|#]', "", name)
    clean_name = clean_name.replace(" ", "_").replace("'", "_").replace('"', "_")
    # Supprimer les underscores doubles ou consécutifs
    clean_name = re.sub(r'_+', '_', clean_name)
    return clean_name.strip('_')

# 1. Récupérer la liste des dernières vidéos avec yt-dlp
ydl_opts = {
    'playlistend': MAX_EPISODES,
    'extract_flat': True,
    'skip_download': True,
    'quiet': True,
}

print(f"Récupération des {MAX_EPISODES} dernières vidéos de la chaîne {CHANNEL_URL}...")
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(CHANNEL_URL, download=False)
        videos = playlist_info.get('entries', [])
except Exception as e:
    print(f"Erreur lors de la récupération des vidéos de la chaîne : {e}")
    sys.exit(1)

if not videos:
    print("Aucune vidéo trouvée. Veuillez vérifier l'URL de la chaîne.")
    sys.exit(1)

print(f"{len(videos)} vidéos listées. Récupération des transcriptions en cours...")

success_count = 0
failed_count = 0

for i, video in enumerate(videos, start=1):
    if not video:
        continue
    video_id = video.get('id')
    title = video.get('title')
    
    if not video_id or not title:
        continue

    # Récupérer la date de publication
    upload_date = video.get('upload_date')
    if upload_date:
        try:
            date_str = datetime.strptime(upload_date, "%Y%m%d").strftime("%Y-%m-%d")
        except ValueError:
            date_str = "Date inconnue"
    else:
        date_str = "Date inconnue"

    filename = f"{date_str}_{sanitize_filename(title)}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    if os.path.exists(filepath):
        print(f"[{i}/{len(videos)}] Déjà récupéré : {title}")
        success_count += 1
        continue

    print(f"[{i}/{len(videos)}] Téléchargement de la transcription : {title} (ID: {video_id})...")

    try:
        # Tenter de récupérer d'abord en français, sinon en d'autres langues ou langues générées
        transcript_list = YouTubeTranscriptApi().fetch(video_id, languages=['fr', 'fr-FR', 'en'])
        
        # Concaténer le texte
        full_text = " ".join([entry.text.replace('\n', ' ') for entry in transcript_list])
        
        # Écrire le fichier Markdown avec les métadonnées YAML
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\n")
            f.write(f"title: \"{title}\"\n")
            f.write(f"date: \"{date_str}\"\n")
            f.write(f"youtube_url: \"https://www.youtube.com/watch?v={video_id}\"\n")
            f.write(f"type: podcast\n")
            f.write(f"---\n\n")
            f.write(full_text)
        
        print(f" -> Enregistré sous {filename}")
        success_count += 1
            
    except Exception as e:
        print(f" -> Échec de la récupération pour '{title}' : {e}")
        failed_count += 1

print(f"\nTerminé ! Succès : {success_count} | Échecs : {failed_count}")
