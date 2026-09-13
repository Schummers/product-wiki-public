# 0001 — Normalisation par extension du schéma source du vault

Date : 2026-07-30
Statut : accepté

## Contexte

Ce domaine est né comme un projet autonome ("Design wiki") avec son propre
schéma : frontmatter `title` / `date` / `youtube_url` / `concepts` sur les
fiches, aucun frontmatter sur les concepts, et une séparation stricte entre le
matériau brut (`raw/sources/`) et la fiche (`wiki/episodes/`).

Le second brain (`../second-brain`) a de son côté un schéma canonique de source
(`_agent/templates/source.md`) : `type` / `name` / `created` / `source_type` /
`status` / `url` / `author`, et met le matériau brut dans la fiche elle-même
(section `## Raw Material`).

Deux corpus doivent cohabiter ici (Parlons Design, Nielsen Norman Group) et la
question d'un branchement futur sur le second brain reste ouverte. Il fallait
donc décider du schéma avant d'ingérer NN/g, puisque migrer des milliers de
fiches après coup coûte cher.

## Décision

Le frontmatter canonique du vault est adopté tel quel, et **étendu** de trois
champs propres à ce domaine :

- `published` — la date de publication par l'éditeur, distincte de `created`
  (date d'ingestion). Le catalogue est trié sur `published`.
- `concepts: []` — liste structurée de concepts candidats, lisible par script.
- `raw:` — chemin vers le fichier de matériau brut.

La séparation raw / fiche est conservée : le matériau brut reste dans
`raw/sources/`, pas dans la fiche.

Les concepts, eux, gagnent un frontmatter qui n'existe nulle part dans le vault
(`type: concept`, `status`, `aliases`), parce qu'ils ne correspondent à aucun
objet du vault.

`published` a par ailleurs été ajouté au template source du second brain, en
champ optionnel : la distinction date de publication / date d'ingestion y est
tout aussi utile.

## Alternatives écartées

**Normalisation stricte** (adopter le schéma du vault sans extension). Écartée :
elle perdait la date de publication, seule façon de juger la fraîcheur d'un
article NN/g de 2016 ; elle remplaçait la liste `concepts` structurée par de la
prose, cassant `generate_index_and_concepts.py` au profit d'un parsing fragile ;
et elle fusionnait des transcripts de 30–50K caractères dans les fiches, ce qui
les rend illisibles dans Obsidian et coûteuses à lire pour un agent, sur un
corpus qui visera plusieurs milliers d'entrées.

**Garder le schéma d'origine.** Écartée : elle interdisait tout branchement
futur sur le vault sans une migration complète, et laissait deux vocabulaires de
frontmatter divergents dans le même AI OS.

## Conséquences

Une fiche de ce domaine est une source valide aux yeux du second brain : un
branchement futur est un déplacement de fichiers, pas une migration de schéma.
En contrepartie, un lecteur qui ne connaît que le vault trouvera ici trois
champs de plus et un matériau brut ailleurs que là où il l'attend — d'où ce
document.
