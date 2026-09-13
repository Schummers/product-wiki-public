---
type: source
name: "#347 Fenêtre modale, le Guide UX Design"
created: 2026-07-30
published: 2024-09-24
source_type: transcript
status: processed
url: https://parlonsdesign.substack.com/p/347-fenetre-modale-le-guide-ux-design
author: Romain Penchenat
raw: raw/sources/2024-09-24_347_Fenêtre_modale,_le_Guide_UX_Design.md
concepts:
  - "Modal Window"
  - "Non-Modal Window"
  - "Accessibility"
  - "Design System"
---

# #347 Fenêtre modale, le Guide UX Design

## 📝 Résumé & Contexte
Cet épisode aborde la fenêtre modale, un composant d'interface souvent surutilisé en design UX. Le présentateur explique les risques liés à son usage, insiste sur l'importance de s'interroger sur sa réelle nécessité et propose des alternatives viables. Enfin, il détaille les bonnes et mauvaises pratiques pour concevoir des modales efficaces et accessibles.

## 💡 Points Clés & Enseignements
* **Une utilisation à questionner systématiquement** : La règle numéro une est de toujours se demander si un autre motif d'interface ne conviendrait pas mieux. Des alternatives comme les fenêtres non modales, les accordéons, les info-bulles ou de simples sous-pages sont souvent plus adaptées et moins intrusives pour l'utilisateur.
* **Les cas d'usage légitimes** : Les modales restent pertinentes pour confirmer des actions irréversibles, afficher l'aperçu rapide d'un contenu depuis une liste, ou encore pour la saisie de formulaires simples à la volée. L'ouverture doit toujours résulter d'une action volontaire de l'utilisateur.
* **Les bonnes pratiques de conception** : Une bonne modale doit être facile à fermer (via un bouton visible et un clic sur l'arrière-plan), avoir un objectif unique et présenter un contenu concis. L'accessibilité est également cruciale, que ce soit pour les lecteurs d'écran ou la navigation au clavier (fermeture via la touche Échap).
* **Les erreurs à éviter** : Il ne faut jamais empiler des modales les unes sur les autres ni les afficher en plein écran (privilégier une page dédiée). De plus, l'affichage automatique de modales à des fins marketing, sans déclenchement de l'utilisateur, est à proscrire car il dégrade fortement l'expérience utilisateur.
* **Nommage dans le Design System** : Pour éviter la multiplication abusive des modales, il est recommandé d'utiliser des noms de composants sémantiques dans le Design System (ex: "confirmation dialog"). Cela limite leur usage aux contextes pour lesquels elles ont été pensées.

## 💬 Citations Marquantes
> "La règle numéro 1 quand on va designer une modale, c'est de se dire est-ce qu'il n'y a pas un autre pattern qui conviendrait mieux à mon action plutôt qu'une modale pour éviter ce piège ?"
> "Ce qui peut être utile à ce moment-là, c'est d'utiliser des noms de composants sémantiques. On ne va pas l'appeler une modal, mais une confirmation dialog, par exemple, qui va indiquer que ça ne doit pas être utilisé à tout va."

## 🔗 Concepts Abordés
* [[Modal Window]] : Composant d'interface s'affichant au-dessus de l'écran et rendant le contenu en arrière-plan inaccessible, souvent utilisé pour demander le focus de l'utilisateur.
* [[Non-Modal Window]] : Alternative qui s'affiche également au-dessus du contenu mais sans bloquer l'interaction avec le reste de l'écran, comme la fenêtre de rédaction d'un email.
* [[Accessibility]] : L'importance de concevoir des composants utilisables par tous, en assurant la compatibilité avec les lecteurs d'écran et la navigation au clavier.
* [[Design System]] : Outil permettant de standardiser les composants ; l'épisode suggère d'y utiliser un nommage sémantique pour guider et limiter l'utilisation des modales.
