# Prompt de session — ingérer un livre

Un livre par session, jamais deux. Colle ce prompt dans une nouvelle session
Claude Code ouverte dans `~/AI OS/compound-learning/product-wiki`, après avoir
remplacé la ligne du livre. Modèle de session : Opus 5 ou Fable 5.1, parce que
les étapes 2 et 3 sont du jugement. Les sous-agents de l'étape 1 tournent en
Haiku 4.5, le skill le rappelle.

Le runbook lui-même vit dans le skill `product-wiki-ingest`, pas ici : ce
prompt ne fait que lancer la session et nommer le livre.

---

Ingère ce livre dans le corpus, en autonomie. Le propriétaire ne suit pas la session.

**Le livre** : `~/Documents/livres/product/Continuous Discovery Habits*.epub`

Invoque le skill `product-wiki-ingest` et suis ses sept étapes. Il porte le
runbook, le modèle par étape et les garde-fous.

Les métadonnées que l'EPUB ne donne pas (date de publication, URL de
référence, auteurs si l'OPF est cassé) se cherchent en ligne. En cas de doute
sur la date, prends celle de l'édition contenue dans l'EPUB et signale-le dans
`wiki/log.md`.

Les autres livres du dossier sont hors périmètre.
