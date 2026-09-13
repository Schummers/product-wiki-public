---
type: source
name: "#366 Le hack secret d'automatisation de Figma"
created: 2026-07-30
published: 2025-02-25
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/366-le-hack-secret-dautomatisation
author: Romain Penchenat
raw: raw/sources/2025-02-25_366_Le_hack_secret_d_automatisation_de_Figma.md
concepts:
  - "Developer Console"
  - "Figma API"
  - "Code Generation"
---

# #366 Le hack secret d'automatisation de Figma

## 📝 Résumé & Contexte
Cet épisode présente une méthode inédite pour automatiser des tâches répétitives dans Figma sans avoir recours à des plugins externes. L'astuce repose sur l'utilisation de la console de développement cachée de l'outil pour exécuter des scripts JavaScript. En s'appuyant sur l'intelligence artificielle pour générer ce code, les designers peuvent gagner un temps précieux sur des modifications complexes.

## 💡 Points Clés & Enseignements
* **La console secrète de Figma** : Figma dispose d'une console de développement cachée accessible via le menu ou des raccourcis (Command K sur Mac). Elle permet d'exécuter du code JavaScript et d'accéder à l'intégralité de l'API dédiée aux plugins.
* **Générer du code avec l'IA** : Il n'est pas nécessaire de savoir coder. Les modèles de langage comme ChatGPT, Gemini ou Claude (recommandé pour de meilleurs résultats) sont excellents pour générer des scripts exploitables dans la console Figma.
* **Cas d'usage pratiques** : Cette méthode permet d'effectuer des sélections complexes (par taille ou radius), d'éditer des propriétés en masse sans variables dédiées, ou de créer rapidement des effets visuels (textes cryptés, skeleton loaders).
* **La structure du prompt idéal** : Pour obtenir un script fonctionnel, le prompt doit demander du "code JavaScript Figma", utiliser le vocabulaire précis du logiciel (frames, auto-layout, etc.) et exiger de ne pas refermer le plugin.

## 💬 Citations Marquantes
> "Et si une fonctionnalité native de Figma vous permettait d'automatiser tout type de tâches, surtout les plus bardantes ?"
> "En quelques secondes, on peut résoudre des problèmes hyper complexes, hyper chiants à gérer à la main avec la console secrète Figma."

## 🔗 Concepts Abordés
* [[Developer Console]] : L'outil natif caché dans Figma permettant d'exécuter des scripts JavaScript directement sur les éléments de design.
* [[Figma API]] : L'interface de programmation permettant de manipuler les designs Figma, exploitée ici sans créer de plugin complet.
* [[Code Generation]] : L'utilisation de modèles de langage (IA) pour rédiger les lignes de code nécessaires à l'automatisation dans Figma.
