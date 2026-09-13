---
type: source
name: "#355 Les 5 astuces Design System de l'équipe Figma"
created: 2026-07-30
published: 2024-12-10
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/355-les-5-astuces-design-system-de
author: Romain Penchenat
raw: raw/sources/2024-12-10_355_Les_5_astuces_Design_System_de_l_équipe_Figma.md
concepts:
  - "Design System"
  - "Pattern Library"
  - "Component Properties"
  - "Design Token Modes"
---

# #355 Les 5 astuces Design System de l'équipe Figma

## 📝 Résumé & Contexte
Dans cet épisode, Romain Pachena analyse une interview de l'équipe Figma détaillant les coulisses de leur propre Design System. L'épisode met en lumière des astuces concrètes de structuration, telles que la gestion des propriétés et l'utilisation des modes. L'objectif est de rappeler qu'un Design System n'est pas qu'une librairie visuelle, mais un outil conçu pour résoudre des problématiques et faciliter la vie des équipes comme des utilisateurs finaux.

## 💡 Points Clés & Enseignements
* **De Component Library à Pattern Library** : Figma appelle son système la 'Figma Pattern Library' (FPL). L'idée est de créer des systèmes répétables basés sur des contextes d'usage sémantiques, plutôt qu'un vaste kit de briques purement visuelles.
* **State Properties vs Context Properties** : L'équipe sépare les propriétés de statut (ex: focus, dictées par l'utilisateur) des propriétés de contexte (ex: avec icône, dictées par le designer). Cette distinction clarifie l'utilisation des composants et évite de manipuler des propriétés inutiles lors du design.
* **Découplage Figma et Code** : Il n'est pas nécessaire d'avoir une correspondance parfaite entre les propriétés dans Figma et celles dans le code. Les contraintes et les utilisateurs (designers vs développeurs) étant différents, chercher l'harmonisation absolue est souvent contre-productif.
* **Usage des Modes pour l'évolutivité** : Pour gérer plusieurs produits avec des identités distinctes (Figma, FigJam, Slide), l'équipe utilise les modes de Figma. Un unique composant s'adapte automatiquement à la charte graphique appropriée en fonction de son contexte.
* **Le rôle fondamental du Design System** : Un Design System ne doit pas être fait pour la beauté de sa structure ou de son code. Son but ultime est toujours d'accélérer la création de valeur et d'améliorer la qualité de vie des utilisateurs finaux et des créateurs.

## 💬 Citations Marquantes
> "le visuel n'est qu'une incarnation d'un système de pensée, de toute une réflexion, et qu'on peut parler design sans avoir à montrer quoi que ce soit."
> "on ne fait pas un design system, on répond à une problématique d'efficience et de qualité de vie."

## 🔗 Concepts Abordés
* [[Design System]] : L'épisode insiste sur le fait qu'il s'agit avant tout d'un outil d'efficience pour accélérer la production de valeur, plutôt que d'un projet purement esthétique.
* [[Pattern Library]] : Une approche conceptuelle où un composant est vu comme une solution sémantique à une problématique d'usage précise, plutôt qu'un simple rendu visuel réutilisable.
* [[Component Properties]] : La structuration des propriétés de composants en distinguant celles liées à l'interaction (statut) de celles liées à la structure de l'interface (contexte).
* [[Design Token Modes]] : L'utilisation des modes natifs de Figma pour automatiser l'adaptation visuelle des composants à travers différentes marques ou sous-produits.
