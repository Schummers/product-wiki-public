# Prompt de session — Pipeline livre (stage 0 à runbook)

Colle ce prompt tel quel dans une nouvelle session Claude Code ouverte dans
`~/AI OS/compound-learning/product-wiki`. Modèle de session : Fable 5.1 (ou Opus 5).
Sous-agents du stage 1 : Haiku 4.5.

---

Tu construis le pipeline livre du vault `~/AI OS/compound-learning/product-wiki`
et tu l'exécutes sur deux livres. Tu travailles en autonomie : le propriétaire ne suit pas cette
session, il prépare un entretien à côté. Tranche toi-même tout ce qui relève du pipeline,
ne lui pose une question que si une décision est irréversible et non couverte ci-dessous.

## Lire d'abord, dans cet ordre

1. `CLAUDE.md`, `SCHEMA.md`, `CONTEXT.md`, `docs/adr/0001` et `docs/adr/0003` (le contrat).
2. Les cinq tickets, dans `~/AI OS/second-brain/projects/tasks/`, qui portent toutes les
   décisions déjà prises et les critères de done. Ils s'exécutent dans cet ordre, chacun
   bloqué par le précédent :
   - `construire-fetch-epub-stage-0-product-wiki.md`
   - `ecrire-les-records-par-chapitre-des-deux-livres-studio.md`
   - `fondre-les-records-livres-dans-la-couche-concepts.md`
   - `creer-le-theme-venture-building-and-studios.md`
   - `documenter-le-runbook-ingerer-un-livre.md`
3. `prompts/stage1-record.md`, `prompts/stage2-write.md`, `prompts/finish-stage2.md`
   (les prompts existants et la leçon d'orchestration : vagues de 3 à 5 agents, jamais plus).
4. `fetch_nngroup.py` (le modèle de script stage 0), `check_records.py`, `verify_wiki.py`,
   `stage2/generate_stubs.py` (à lire, **à ne jamais relancer** : il réécrit toutes les pages
   concept et effacerait les 147 `developed`), `stage3/generate_themes.py`.

## Les deux livres

Dans `~/Documents/livres/product/`, ne jamais les copier sous `~/AI OS/` :

- `Startup Studio Playbook*.epub` — Attila Szigeti, publié 2019-02-17,
  url `https://www.amazon.com/dp/B07NVNYM4C`, slug `startup-studio-playbook`.
  EPUB natif, un fichier HTML par chapitre.
- `Venture Studios Demystified*.epub` — Shilpa Kannan et Mitchel Peterman, publié 2022-02-08,
  url `https://www.amazon.com/dp/B09SL5GSQN`, slug `venture-studios-demystified`.
  Né d'un PDF : OPF cassé (titre = hash, auteur = Unknown), aucun titre HTML, chapitres
  repérés par les ancres `page_N` du NCX, lignes coupées et césures à recoller
  (`--rejoin-lines`).

Topics pour les deux : `venture-studio, startup, product-strategy`.

## Décisions déjà prises (ne pas rouvrir)

- Un livre = N raw = N records, un par chapitre, à plat dans `raw/sources/` et
  `wiki/episodes/`, nommés `<published>_<book-slug>_<NN>-<chapter-slug>.md`.
- Texte intégral versionné en git, verbatim. L'EPUB est le seul format d'entrée.
- Découpage piloté par le NCX, pas par les titres HTML.
- `developed` exige le seuil de records habituel **et** au moins deux ouvrages distincts.
- Le venture building appartient au corpus : nouveau thème `Venture Building and Studios`,
  hors `PLAYBOOK_THEMES`.
- Anglais pour tout ce qui est nouveau (ADR 0002). Zéro fabrication (SCHEMA.md règle 1).

## Méthode

- Un ticket à la fois, dans l'ordre. Chaque ticket se termine par ses gates verts
  (`check_records.py`, `verify_wiki.py`) et un commit conventionnel, message dans le ticket.
- `--dry-run` avant toute écriture de raw ; relis le plan de découpe et corrige les options
  avant d'écrire.
- Stage 1 : sous-agents Haiku 4.5, lots de 5 chapitres, 3 à 5 agents par vague, vérification
  et commit entre deux vagues. Pilote de 3 chapitres avant le reste.
- Stage 2 et 3 : ton propre jugement (modèle de session), pas un sous-agent léger.
- Si la session approche de sa limite : committe ce qui est propre, note l'état dans
  `wiki/log.md`, arrête-toi proprement. Le travail est reprenable ticket par ticket.

## Clôture

1. Quand un ticket est fini, mets son `status: done` dans le fichier de tâche du second brain
   et une ligne datée dans son `## Journal` (le skill `update-brain` le fait aussi, en fin
   de session).
2. À la toute fin, propose `/update-brain` pour redescendre l'état, et liste en trois lignes
   ce que le livre suivant devra faire différemment, s'il y a quelque chose.

## Hors périmètre

- Les 13 autres livres du dossier. Les deux tickets de backlog attendent le runbook.
- `wiki/playbooks/` : aucun playbook pour le nouveau thème.
- Tout usage de ce corpus pour son entretien : ça se décide après, pas ici.
- Le second brain : tu n'y écris que le statut et le journal des cinq tickets.
