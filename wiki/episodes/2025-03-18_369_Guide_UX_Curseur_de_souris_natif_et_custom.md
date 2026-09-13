---
type: source
name: "#369 Guide UX : Curseur de souris natif et custom ?"
created: 2026-07-30
published: 2025-03-18
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/369-guide-ux-curseur-de-souris-natif
author: Romain Penchenat
raw: raw/sources/2025-03-18_369_Guide_UX_Curseur_de_souris_natif_et_custom.md
concepts:
  - "Native Cursor"
  - "Custom Cursor"
  - "Discoverability"
  - "Accessibility"
---

# #369 Guide UX : Curseur de souris natif et custom ?

## 📝 Résumé & Contexte
Cet épisode de Parlons Design explore l'importance du curseur de la souris dans la conception d'interfaces, un élément central mais souvent négligé. Romain Bajna détaille comment les curseurs natifs peuvent améliorer instantanément la découvrabilité des actions avec peu d'effort. Il aborde également les cas d'usage justifiant un curseur sur mesure, tout en mettant en garde sur les défis techniques et d'accessibilité associés.

## 💡 Points Clés & Enseignements
* **Exploiter les curseurs natifs** : Les curseurs par défaut (pointeur de sélection, d'édition de texte ou main cliquable) sont des standards du web universellement compris. Les configurer correctement via une simple ligne de CSS résout de nombreux problèmes de compréhension.
* **Indiquer des statuts ou interactions invisibles** : Utiliser curseurs comme « not allowed » (interdit), « busy » (chargement) ou « grab » (drag and drop) permet d'expliquer intuitivement les limites du système ou la possibilité d'interagir avec des éléments complexes.
* **L'usage des curseurs sur mesure** : Créer un curseur 100% personnalisé est complexe mais justifié pour des outils d'édition visuelle (pour afficher l'outil sélectionné), la collaboration en temps réel, ou la data visualisation poussée.
* **Contraintes techniques et accessibilité** : Un curseur custom requiert un soin particulier sur les contrastes, la précision parfaite du clic et la gestion de multiples états. De plus, l'interface ne doit jamais dépendre exclusivement de la souris pour rester accessible.

## 💬 Citations Marquantes
> "Le curseur de souris, un élément incontournable mais trop souvent oublié lors de la phase de design."
> "S'il y a des soucis de découvrabilité sur des fonctionnalités, souvent changer le curseur est une très bonne façon d'améliorer la découvrabilité en un instant avec à peu près aucun downside."
> "Quand on design un curseur sur mesure, on n'a pas un seul état à designer. On en a 3, 4, 5, voire plus."

## 🔗 Concepts Abordés
* [[Native Cursor]] : L'utilisation de curseurs par défaut gérés par le navigateur (comme le pointer, text ou grab) permettant d'indiquer de manière standard les interactions possibles.
* [[Custom Cursor]] : Le remplacement du curseur natif par un élément codé spécifiquement pour répondre à des besoins d'édition avancés, de collaboration ou d'identité visuelle.
* [[Discoverability]] : La capacité pour un utilisateur de deviner intuitivement les interactions possibles, facilitée par l'affichage d'un curseur de souris approprié au survol.
* [[Accessibility]] : La nécessité de proposer des alternatives de navigation (clavier, écrans tactiles) afin de ne pas rendre l'usage d'un produit dépendant uniquement de la souris.
