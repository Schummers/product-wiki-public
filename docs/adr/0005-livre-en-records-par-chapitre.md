# 0005 — Un livre entre dans le corpus comme N records, un par chapitre

Date : 2026-09-03
Statut : accepté, implémenté (`fetch_epub.py`, deux livres ingérés)

## Contexte

Le corpus n'avait jamais ingéré de livre. Ses trois scripts de stage 0
(`fetch_nngroup.py`, `fetch_podcasts.py`, `fetch_substack_transcripts.py`)
prennent des articles et des transcripts : une source, un raw, un record. Un
livre de 170 à 230 000 caractères ne tient pas dans ce moule. Le stage 1
tourne sur un modèle léger qui ne peut pas résumer fidèlement un livre entier
en 3 à 6 concepts, et une page concept ne peut pas citer « ce que dit le
livre » en bloc : la règle de bidirectionnalité (`SCHEMA.md`, règle 4) veut
un record précis derrière chaque contribution.

Treize livres attendent dans la bibliothèque, sur le produit, la recherche et
le venture building. Il fallait un moule qui tienne pour tous, décidé avant
le premier, parce que renommer cinquante raw après coup coûte plus que de
choisir maintenant.

## Décision

**Un livre = N raw = N records, un par chapitre.** Le raw et le record
portent le livre en frontmatter (`book`, `book_slug`, `part`, `chapter`,
`chapter_number`) et le nommage groupe les chapitres :
`raw/sources/<published>_<book-slug>_<NN>-<chapter-slug>.md`. Les fichiers
restent à plat dans `raw/sources/` et `wiki/episodes/`, parce que tous les
scripts existants globent ces dossiers à plat.

**Le texte intégral est versionné en git, verbatim**, comme le reste de
`raw/`. Tranché le 2026-09-03 : le repo est privé, et s'il faut
un jour le partager, on le recrée sans cet historique. Aucun EPUB sous
`AI OS/` (décision du 2026-08-12, inchangée) : le fichier reste dans la
bibliothèque hors AI OS, seul le texte extrait entre.

**L'EPUB est le seul format d'entrée.** Un PDF converti en EPUB par Calibre
est accepté tel quel et le script absorbe ses défauts (`--rejoin-lines` :
lignes coupées, césures, numéros de page, en-têtes courants). On ne maintient
pas un second extracteur PDF.

**Le découpage est piloté par la table des matières NCX**, pas par les titres
HTML. Un EPUB Calibre né d'un PDF n'a aucun `<h1>`, seulement des ancres
`page_N` visées par le NCX ; *Venture Studios Demystified* tient en quatre
fichiers HTML. L'ordre est celui du document (spine, puis position de
l'ancre), jamais `playOrder`, faux dans ce même livre.

**Le seuil `developed` compte les ouvrages, pas seulement les records.** Un
concept cité par huit chapitres du même livre a huit sources au sens du
compteur mais un seul ouvrage. `developed` exige le seuil habituel de records
**et** au moins deux ouvrages distincts (deux livres, ou un livre et des
articles). Sans cette règle, un seul livre bien découpé fabriquerait des
pages « cross-source » qui ne le sont pas.

## Alternatives écartées

**Un record par livre.** Écartée : trop gros pour le stage 1, et une page
concept ne pourrait pas dire quel chapitre soutient quelle affirmation.

**Raw gitignoré, texte hors git.** Écartée : `raw/` est ce qui rend le corpus
auditable (`check_records.py` vérifie les citations contre lui). Un raw absent
du clone casse le gate.

**Un extracteur PDF dédié.** Écartée : Calibre fait déjà la conversion, et
mieux à mesure de ses versions. Le script se contente de réparer ce que la
conversion laisse.

**Couper sur les titres HTML.** Écartée : ils n'existent pas dans un EPUB né
d'un PDF, et dans un EPUB natif ils ne correspondent pas toujours à la table
des matières (Calibre les enveloppe dans des `<blockquote>`).

## Ce qui a changé en cours de route

- Les segments courts (intercalaires « Part I ») fusionnent dans le chapitre
  suivant, comme prévu, mais un chapitre court non intercalaire aussi
  (*Raising a Fund*, 700 caractères, absorbé par *Studio Structure*). Le
  dry-run le montre, on décide à la lecture du plan.
- Deux options de plus que prévu : `--absorb` (fusionner un segment dans le
  chapitre précédent, pour une tear sheet ou une intro en trois morceaux) et
  `--relabel` (réparer un libellé NCX tronqué, « art 1: » pour « Part 1: »).
- La cible d'une entrée NCX par page est déplacée vers la ligne qui porte le
  titre du chapitre quand elle existe sur la même page : le NCX d'un PDF
  pointe le haut de la page, pas le titre, et la coupe tombait au milieu du
  paragraphe précédent.
- Résidu assumé : les tableaux et figures d'un EPUB né d'un PDF sortent en
  lignes détachées. Le texte courant, lui, est recollé.

## Conséquences

- `SCHEMA.md` gagne les champs livre et la règle des deux ouvrages ;
  `CONTEXT.md` distingue l'ouvrage (unité bibliographique) du record de
  chapitre (unité du pipeline).
- Le stage 2 doit fonder les records de manière incrémentale
  (`stage2/fold_records.py`) : `generate_stubs.py` réécrit toutes les pages et
  effacerait les 147 `developed`.
- Le nombre de records par livre dépend du dry-run, donc d'un jugement
  humain ou agent au moment de l'ingestion. Le runbook (`CLAUDE.md`,
  « Ingesting a book ») fixe la séquence pour que ce jugement reste le seul
  point non mécanique.
