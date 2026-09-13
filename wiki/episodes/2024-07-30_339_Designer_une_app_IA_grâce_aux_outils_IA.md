---
type: source
name: "#339 Designer une app IA grâce aux outils IA"
created: 2026-07-30
published: 2024-07-30
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/338-designer-une-app-ia-grace-aux
author: Romain Penchenat
raw: raw/sources/2024-07-30_339_Designer_une_app_IA_grâce_aux_outils_IA.md
concepts:
  - "Local LLM"
  - "Web Performance"
  - "Generative UI Assets"
---

# #339 Designer une app IA grâce aux outils IA

## 📝 Résumé & Contexte
Romain Parchenap présente les apprentissages tirés de la création d'Estoire, une application iOS générant des histoires pour enfants. Il y explique les défis de faire fonctionner un modèle de langage (LLM) en local sur un smartphone et partage les différents outils d'intelligence artificielle utilisés pour concevoir rapidement ce MVP.

## 💡 Points Clés & Enseignements
* **Avantages et contraintes d'un LLM en local** : L'utilisation d'un modèle d'IA en local améliore la confidentialité des données et annule les coûts de serveurs. La contrainte principale est la limitation matérielle de l'appareil, ce qui impose d'utiliser un modèle léger mais efficace.
* **Choix du modèle et intégration** : Après plusieurs essais, le modèle Fi 3 a été choisi pour son bon rapport poids/qualité. L'auteur a décidé d'embarquer directement le modèle de 2Go dans l'application pour être transparent avec les utilisateurs dès le téléchargement.
* **Optimisation de l'UX face à la lenteur** : Pour masquer les temps de génération de l'IA locale, l'application utilise une expérience paginée : la première page est affichée rapidement, et les suivantes se génèrent pendant la lecture. Des écrans de chargement animés font aussi patienter l'utilisateur.
* **Accélération du design avec l'IA** : Des outils comme ChatGPT Audio ont aidé à l'exploration du concept. Adobe Firefly et Canva ont permis de générer très rapidement l'icône, les personnages et les visuels de chargement, suffisant amplement pour un MVP.

## 💬 Citations Marquantes
> "On ne va pas appeler l'API de chat GPT ni payer OpenAI pour ça, on va le faire tourner directement sur le téléphone de l'utilisateur."
> "Si on peut réduire les coûts de production [...] on peut se permettre soit de rendre le produit complètement gratuit, soit de le vendre beaucoup moins cher, et donc de proposer une meilleure expérience."

## 🔗 Concepts Abordés
* [[Local LLM]] : L'exécution d'un modèle de langage de petite taille directement sur l'appareil mobile de l'utilisateur.
* [[Web Performance]] : L'utilisation d'artifices de design (pagination, loaders visuels) pour minimiser la perception d'attente face aux temps de traitement d'une IA locale.
* [[Generative UI Assets]] : L'exploitation d'outils de génération d'images pour produire en quelques minutes les illustrations et l'icône d'un produit en phase MVP.
