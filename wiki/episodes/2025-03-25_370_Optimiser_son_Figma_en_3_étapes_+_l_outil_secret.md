---
type: source
name: "#370 Optimiser son Figma en 3 étapes + l'outil secret"
created: 2026-07-30
published: 2025-03-25
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/optimiser-son-figma-en-3-etapes-loutil
author: Romain Penchenat
raw: raw/sources/2025-03-25_370_Optimiser_son_Figma_en_3_étapes_+_l_outil_secret.md
concepts:
  - "Flatten"
  - "Hidden Layers"
  - "Component Properties"
  - "Memory Usage"
---

# #370 Optimiser son Figma en 3 étapes + l'outil secret

## 📝 Résumé & Contexte
Cet épisode traite des problèmes de performances dans Figma qui réduisent la productivité et la qualité du design. Romain Benchna y partage trois catégories de bonnes pratiques pour optimiser un fichier : la gestion du contenu, la simplification des composants et l'organisation du fichier. Il dévoile également un outil natif caché permettant de localiser précisément les éléments qui consomment trop de mémoire.

## 💡 Points Clés & Enseignements
* **Optimisation du contenu et des images** : Il est crucial d'aplatir les formes vectorielles complexes pour en faire un seul calque. De plus, il faut compresser les images avant de les importer ou utiliser des plugins comme Downsize, et supprimer les calques cachés qui consomment inutilement des ressources.
* **Simplification des composants** : Les composants possédant des centaines de variantes ou des dépendances imbriquées trop profondes ralentissent considérablement l'outil. Il est conseillé de privilégier l'usage des propriétés pour limiter le nombre de variantes et d'éviter les liaisons non conventionnelles entre fichiers.
* **Organisation et division des fichiers** : Une bonne pratique consiste à diviser son fichier en utilisant des pages dédiées pour chaque étape du processus ou pour les archives. Si cela ne suffit pas, il faut scinder le projet en plusieurs petits fichiers moins lourds.
* **L'outil Memory Usage** : Caché dans le menu 'View', cet outil permet d'afficher la jauge de mémoire consommée par Figma. En activant 'Manage Memory', il est possible de voir exactement quel pourcentage de mémoire est utilisé par chaque calque directement dans le panneau dédié.

## 💬 Citations Marquantes
> "Un fichier Figma lent, on en a tous connu un, ou plusieurs, et c'est un véritable enfer."
> "Un fichier lent, c'est souvent un fichier dans lequel on va essayer de réduire notre temps de travail de manière souhaitée ou même sans s'en rendre compte."
> "Un fichier Figma bien pensé, c'est censé être efficient. S'il y a des problèmes de perf, c'est qu'il y a probablement des merdes qui les causent."

## 🔗 Concepts Abordés
* [[Flatten]] : Action de transformer des formes complexes (SVG, masques) en un seul calque pour réduire la charge de calcul et augmenter les performances de Figma.
* [[Hidden Layers]] : Calques invisibles qui continuent de consommer de la puissance de calcul s'ils ne sont pas supprimés du fichier.
* [[Component Properties]] : Fonctionnalité permettant de réduire le nombre de variantes d'un composant et d'améliorer les performances globales du fichier.
* [[Memory Usage]] : Indicateur de performance natif dans Figma permettant de diagnostiquer l'impact de chaque calque sur la mémoire vive.
