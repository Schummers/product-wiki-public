# 0003 — La couche thème est un routeur pour agent, pas une MOC pour humain

Date : 2026-08-21
Statut : accepté

## Contexte

Le corpus contient 954 records et 384 pages concept, dont 147 `developed` de
3000 à 6000 mots chacune, sourcées et attribuées. Le savoir est là. Ce qui
manquait, c'est le chemin : rien ne conduisait une question vers la bonne page.

Le seul index existant, `wiki/index.md`, fait 220 Ko et liste 954 sources à
plat. Il est utile à un humain qui parcourt le corpus, inutile pour router : le
charger coûte tout le budget de contexte sans rien décider.

Objectif visé : quand on conçoit une interface et se pose une question
(hiérarchie d'information, best practices mobile, méthodes de navigation en SaaS
B2B complexe), un agent trouve la réponse dans le corpus plutôt que dans ses
propres a priori.

## Décision

Une couche `wiki/themes/` : 21 thèmes, `type: theme`, plus `_router.md`.

**Elle est conçue pour un agent, pas pour la lecture humaine.** Le propriétaire a
tranché : il ne lira pas ce corpus dans Obsidian. Conséquence directe sur la
forme, le routeur fait 594 mots là où une MOC de navigation en ferait plusieurs
milliers.

Échelle d'information à quatre rangs, chacun pointant vers le suivant :

| Rang | Fichier | Taille |
|---|---|---|
| 1 | `_router.md`, 21 déclencheurs | 594 mots |
| 2 | page thème, concepts glosés | ~600 mots |
| 3 | page concept | 3000-6000 mots |
| 4 | record, puis `raw/` | variable |

**Génération et jugement sont séparés.** `stage3/theme_map.py` porte la
curation (thème vers concepts de rang 1), `stage3/theme_prose.py` porte le
jugement écrit par un modèle fort (le déclencheur du thème, la glose de chaque
concept), `stage3/generate_themes.py` assemble. Regénérer après une ingestion
rafraîchit les compteurs et le rang 2 sans toucher une ligne écrite par un
modèle. C'est le même principe que `stage2/merge_map.py`.

**Le rang 2 n'est pas curé.** Les stubs et concepts à source unique sont
rattachés à un thème via les records qu'ils partagent avec les concepts de rang
1. Une ingestion les reclasse seule.

Noms de thèmes en **anglais ASCII**, et jamais égaux à un nom ou alias de
concept. Deux raisons : l'ADR 0002 fait de l'anglais la langue du corpus, et
l'étape 2 avait déjà dû réparer des liens cassés par des accents précomposés.
`verify_wiki.py` refuse une collision de nom, qui rendrait un wikilink ambigu.

## Alternatives écartées

**Une MOC à la Nick Milo (LYT).** Pensée pour un humain qui flâne. Le propriétaire ne
flânera pas. Une page de navigation agréable à lire est un mauvais routeur : la
prose dilue les déclencheurs.

**Un RAG vectoriel.** Sur 147 pages, un routeur textuel est plus simple,
déterministe, auditable et versionné dans git. Surtout, un embedding ne dit
jamais *pourquoi* il a envoyé là, alors qu'une ligne de déclencheur se relit et
se corrige.

**Un fichier unique `wiki/map.md`.** Aucun changement de schéma, mais il
redevient un pavé à mesure que le corpus grossit, c'est-à-dire exactement le
défaut d'`index.md` reproduit un rang plus haut.

**Des thèmes taillés par situation de design** ("composer une landing page")
plutôt que par discipline. Ça routerait mieux les questions réelles du propriétaire,
qui sont task-shaped, mais ça laisse des trous : un découpage par situation ne
couvre pas exhaustivement 147 concepts. Retenu à la place : thèmes par
discipline pour la couverture, et `_router.md` qui absorbe la traduction
question vers thème.

## Conséquences

- Ajouter une source ne périme pas la couche : `generate_themes.py` la
  reconstruit. Le jugement survit.
- `SCHEMA.md` gagne un troisième type. `verify_wiki.py` gagne trois contrôles,
  dont « tout concept `developed` appartient à au moins un thème », qui rend
  visible un trou qui serait sinon silencieux.
- Modifier un fichier de `wiki/themes/` à la main est perdu à la prochaine
  génération. Le point d'édition est `stage3/theme_prose.py`.
- Les 21 thèmes sont un découpage assumé, pas une vérité. Le propriétaire n'a pas
  validé la liste avant génération (session en autonomie) : elle est à relire.

## Effet de bord : le gate d'intégrité redevient utile

En instrumentant la couche, `verify_wiki.py` a été repris. Il signalait 1701
problèmes, dont 1700 étaient les liens cassés assumés vers les concepts à source
unique. Un gate rouge en permanence n'attrape aucune régression.

Règle ajoutée, qui se dérive du corpus seul : un nom cité par **un** record sans
page est normal (l'étape 2 ne crée une page qu'à partir de deux sources) ; le
même nom cité par **deux ou plus** est un vrai manque. Le gate passe à 0.

Deux vrais défauts se cachaient sous ce bruit, corrigés :
`Creative Problem Solving`, cité par deux records sans page, absorbé en alias
d'`Ideation` ; `E-Commerce` ne listait pas `2020-11-08_augmented-reality-useful`
dans ses `## Sources`.
