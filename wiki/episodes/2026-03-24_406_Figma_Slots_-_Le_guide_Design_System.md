---
type: source
name: "#406 Figma Slots - Le guide Design System"
created: 2026-07-30
published: 2026-03-24
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/406-figma-slots-le-guide-design-system
author: Romain Penchenat
raw: raw/sources/2026-03-24_406_Figma_Slots_-_Le_guide_Design_System.md
concepts:
  - "Figma Slots"
  - "Design System"
  - "Placeholder"
  - "Auto Layout"
---

# #406 Figma Slots - Le guide Design System

## 📝 Résumé & Contexte
Cet épisode détaille les Figma Slots, une nouvelle fonctionnalité offrant une flexibilité accrue pour la gestion du contenu au sein des composants. Romain Pachna y explique les cas d'usage principaux, la méthode pour les intégrer efficacement, ainsi que les bonnes pratiques pour ne pas compromettre la rigueur d'un Design System.

## 💡 Points Clés & Enseignements
* **Cas d'usage principaux** : Les slots sont particulièrement utiles pour les composants de structure (modales, sidebars) et de listing (tableaux, listes). Ils permettent d'avoir une structure de base stable tout en conservant une zone de contenu hautement dynamique et personnalisable.
* **Fin de la méthode des placeholders** : Auparavant, il fallait utiliser des composants placeholders complexes à remplacer ou détacher l'instance, ce qui générait de la dette technique. Les slots remplacent cette méthode archaïque en offrant un espace natif et maintenable.
* **Contraintes et paramètres fixes** : Lors de la création d'un slot, ses dimensions et sa règle d'auto-layout sont fixées et ne pourront plus être modifiées par l'utilisateur du composant. Une configuration rigoureuse est donc nécessaire dès le départ.
* **Guidage des utilisateurs** : Il est recommandé de nommer clairement les slots, de proposer des composants recommandés et de pré-remplir le contenu par défaut. Il faut aussi veiller à ne pas multiplier les slots dans un même composant pour ne pas perdre la notion de contrainte.
* **Alignement technique** : Le concept de slot est très proche de la notion de 'children' utilisée en développement web et mobile (React, Vue). Il est conseillé de s'aligner avec les équipes techniques pour garder des composants identiques entre le design et le code.

## 💬 Citations Marquantes
> "Avant les slots, la technique qu'on utilise souvent dans les composants, c'est qu'on crée un composant placeholder [...] ça créait clairement une dette technique d'un truc pas très maintenable."
> "Attention, ça peut faire glisser votre design système vers un surplus de liberté et donc en perdre un petit peu son intérêt."

## 🔗 Concepts Abordés
* [[Figma Slots]] : Zone réservée au sein d'un composant Figma permettant d'injecter du contenu libre sans détacher l'instance.
* [[Design System]] : L'usage des slots doit être contrôlé pour éviter que le système ne devienne trop permissif et perde sa valeur de standardisation.
* [[Placeholder]] : Ancienne technique de contournement utilisant des faux composants pour laisser de la place, désormais remplacée par les slots.
* [[Auto Layout]] : La configuration de l'auto-layout dans un slot est figée à la création et dicte comment le contenu ajouté s'organisera.
