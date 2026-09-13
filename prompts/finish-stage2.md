# Prompt de session — Terminer product-wiki (étape 2 : rédaction des concepts)

Colle ce prompt tel quel dans une nouvelle session Claude Code ouverte dans `~/AI OS/product-wiki`.

---

Tu termines l'étape 2 du pipeline du vault `~/AI OS/compound-learning/product-wiki`.

## Lire d'abord

1. `CLAUDE.md` et `SCHEMA.md` (le contrat : templates, règles, qui écrit quoi).
2. `stage2/post_merge_counts.txt` (nombre de sources par concept, trié).

## État committé (ne pas refaire)

- 954 fiches sources dans `wiki/episodes/`, toutes vérifiées.
- Fusion des concepts faite (`stage2/merge_map.py` + `stage2/singleton_map.py`, appliquées).
- 384 pages concept dans `wiki/concepts/`, générées avec frontmatter, aliases et section `## Sources` annotée. Toutes en `status: stub`, section Definition vide.
- Index régénéré, `verify_wiki.py` sans collision. Les ~851 liens `[[...]]` vers des concepts à 1 seule source sont des liens cassés ASSUMÉS : ne pas créer ces pages.

## Travail restant : rédiger les concepts à 5+ sources (~147)

Liste : `awk -F'\t' '$1>=5 {print $2}' stage2/post_merge_counts.txt`. Les 2-4 sources restent stubs (statut légitime, ne pas les rédiger).

Pour chaque concept, un agent (modèle fort — le modèle de session, PAS Haiku) :

1. Lit la page `wiki/concepts/<Nom>.md` : sa liste `## Sources`.
2. Ouvre chaque fiche source listée (`wiki/episodes/<basename>.md`) : Summary, Key Takeaways, la ligne Concepts correspondante. Ne JAMAIS ouvrir `raw/`.
3. Écrit dans la page :
   - `## Definition` : synthèse générale du concept tel que les sources le décrivent (1-2 paragraphes).
   - `## Practice` : compilation structurée des recommandations des sources, sous-titres si utile. Attribué : si deux sources divergent, le dire, ne pas trancher.
   - Ne touche PAS à la section `## Sources` ni aux aliases.
   - Frontmatter : `status: developed`, `updated: <date du jour>`.
4. Règles absolues (SCHEMA.md) : anglais, zéro invention (rien que ce que les sources disent), attribution jamais effacée, wikilinks internes seulement.

## Orchestration (leçon des sessions précédentes : la limite de session tue les rafales)

- Trancher par lots de ~10 concepts par agent, du mieux sourcé au moins sourcé. Les 10 plus gros (30+ sources) : 3-4 concepts par agent max.
- **Vagues de 3-5 agents maximum, jamais plus.** Attendre la fin d'une vague, vérifier, committer, puis vague suivante.
- Vérification par vague : `python3 verify_wiki.py` (0 collision attendu) + relire 1 page au hasard (sections présentes, status passé à developed, Sources intacte).
- Commit par vague : `feat(etape2): concepts rediges <noms ou plage>`.
- Si la limite de session approche ou que des agents meurent : committer ce qui est propre et s'arrêter proprement. Le travail est reprenable (les pages restées `stub` sont la todo).

## Clôture (une fois les ~147 en `developed`)

1. `python3 generate_index_and_concepts.py` puis `python3 verify_wiki.py`.
2. Mettre à jour `wiki/log.md` : une entrée datée résumant l'étape 2 (fusion + rédaction, chiffres).
3. Passer les fiches sources en `status: processed` (script sed/python simple, elles ont toutes été foldées) et re-committer.
4. Commit final : `feat(etape2): COMPLETE`.
5. Proposer `/update-brain` pour redescendre l'état dans le second brain.

## Hors périmètre

- Étape 3 (synthèses) : à la demande uniquement, jamais automatique (SCHEMA.md). Ne pas la lancer.
- Traduction des fiches Parlons Design : différée, ne pas y toucher.
- Nouveaux corpus : hors sujet.
