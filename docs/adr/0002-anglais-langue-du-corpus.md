# 0002 — L'anglais comme langue du corpus, et la migration des concepts

Date : 2026-07-30
Statut : accepté

## Contexte

Le premier corpus (Parlons Design) est en français : 90 fiches et 253 concepts
écrits en français. Le second (Nielsen Norman Group) est en anglais et sera bien
plus volumineux.

Les fiches sont propres à un corpus, mais **les concepts sont partagés** : une
fiche française et une fiche anglaise pointent vers le même concept. Laisser deux
langues dans `wiki/concepts/` recrée mécaniquement les doublons que la règle
anti-doublons cherche à empêcher (`Accessibilité.md` face à `Accessibility.md` —
le vault en contenait déjà deux variantes avant NN/g).

## Décision

L'anglais est la langue du corpus pour tout le contenu nouveau, et **la langue
unique de la couche concepts**.

Les 253 concepts existants sont renommés en anglais lors de la passe de
dédoublonnage, avant l'ingestion NN/g. Leur nom français d'origine est conservé
en `aliases`, ce qui garde la recherche en français fonctionnelle et empêche
qu'un futur agent recrée le concept sous son ancien nom.

Les 90 fiches Parlons Design restent en français. Leur traduction est différée
sans échéance.

## Alternatives écartées

**Tout en français.** Écartée : elle imposait de traduire chaque article NN/g à
l'ingestion, sur le corpus le plus volumineux, en introduisant une couche de
paraphrase entre la source et la fiche — exactement ce que la règle de
non-fabrication cherche à éviter.

**Concepts bilingues** (nom français et nom anglais coexistant). Écartée : c'est
la définition du doublon, avec une divergence de contenu garantie à terme.

**Traduire les fiches Parlons Design tout de suite.** Écartée : purement
cosmétique, elle ne débloque rien et coûte 90 passes de modèle. Les concepts
suffisent à faire le pont entre les deux corpus.

## Conséquences

La couche concepts est homogène et reste dédoublonnable à l'échelle de plusieurs
milliers de sources. Le prix est un vault visiblement mixte pendant un temps
indéterminé : des fiches françaises pointant vers des concepts anglais. C'est
assumé, et l'alias français est ce qui rend la chose navigable.
