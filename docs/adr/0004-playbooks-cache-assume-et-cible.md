# 0004 — Les playbooks sont un cache assumé, et seulement sur les thèmes de revue

Date : 2026-08-21
Statut : accepté, implémenté (6 playbooks sur 6)

## Contexte

Deux usages du corpus, et ils ne veulent pas la même chose.

Un agent **conseil** répond à une question de conception. La nuance attribuée
est exactement sa valeur : les pages concept, avec leurs désaccords signalés et
leurs sous-sections, lui conviennent telles quelles.

Un agent **revue** confronte un écran à des règles. Il lui faut des règles
cochables et un critère d'exhaustivité du type « chaque règle a un verdict ».
Ce critère ne s'accroche pas à 6000 mots de prose : on ne peut pas dire d'un
paragraphe qu'il est `holds` ou `breached`. Une revue adossée directement aux
pages concept sera consciencieuse et non exhaustive, et surtout personne ne
saura ce qu'elle a omis.

Le skill `writing-for-agents` nomme précisément l'objet en jeu : un document qui
recopie une source de vérité est un **cache**, et un cache ne mérite sa charge
que si la consultation directe est coûteuse.

## Décision

Des **playbooks** dans `wiki/playbooks/`, `type: playbook` : les règles d'un
thème, formulées de façon assertive et vérifiable, chacune attribuée.

Trois contraintes reprises du contrat du vault :

1. **Formulation positive.** La règle dit l'état visé, pas l'interdit. Une
   interdiction rend le comportement interdit plus disponible, pas moins.
2. **Désaccord signalé, jamais arbitré.** Un playbook qui tranche entre deux
   sources ment sur le corpus. Les pages concept signalent déjà leurs
   désaccords ; le playbook les porte.
3. **Attribution jusqu'au record** quand le corpus la donne, jusqu'à la page
   concept sinon, et le playbook dit lequel des deux niveaux il utilise.

**Seulement 6 thèmes sur 21**, listés dans `stage3/theme_map.PLAYBOOK_THEMES` :
heuristiques et évaluation, composition de page, interaction et patterns,
accessibilité, mobile, structure et navigation. Ce sont ceux contre lesquels une
revue de design tourne réellement. Un playbook « Carrière et portfolio » ne
servirait aucune revue. Les 15 autres thèmes restent en navigation seule, et le
skill de revue sait lire leurs pages concept quand un thème hors liste entre
dans le périmètre.

## Le risque, et ce qui le rend visible

Un cache dérive en silence. Nouvelle source, page concept mise à jour, playbook
périmé sans que rien ne le dise. C'est le seul vrai coût de cette décision.

Garde-fou : chaque playbook déclare `sources_as_of`, et
`stage3/check_playbooks.py` compare cette date au champ `updated` de chaque
concept listé. Un concept plus récent que le playbook le fait sortir en `STALE`,
avec sortie 1 pour pouvoir servir de gate. Le script signale aussi les concepts
du thème qu'un playbook aurait oubliés, et les playbooks planifiés non encore
écrits.

La dérive reste possible entre deux exécutions du script. Elle n'est plus
silencieuse.

## Alternatives écartées

**Distiller les 21 thèmes.** Volume de tokens attirant, mais 15 documents que
personne ne lirait, chacun à maintenir contre sa dérive. Le cache doit être payé
là où la consultation est coûteuse, pas partout.

**Pas de playbook du tout, l'agent lit les concepts.** Fraîcheur automatique,
zéro duplication. Écarté pour le seul cas de la revue, où l'absence de critère
d'exhaustivité vérifiable est rédhibitoire. C'est la piste retenue pour les 15
autres thèmes.

**Écrire les synthèses dans les pages concept** (`## Synthesis`, statut
`synthesized` prévu par `SCHEMA.md`). Ç'aurait évité un nouveau type de
document, mais mélangé deux publics dans un même fichier : la page concept
sert le conseil, le playbook sert la revue, et les tailles visées diffèrent d'un
facteur cinq.

## État

Les 6 playbooks planifiés sont écrits, chacun distillé d'une lecture intégrale
de ses pages concept sources plutôt que d'un résumé :

| Playbook | Règles | Concepts sources |
|---|---|---|
| Usability Heuristics and Evaluation | 18 (10 heuristiques + 8 règles d'évaluation) | 9, dont les dix heuristiques de Nielsen |
| Accessibility and Inclusion | 20 | 4 |
| Page Composition and Hierarchy | 20 | 8 |
| Interaction and Interface Patterns | 35 | 12 |
| Mobile and Multi-Device | 25 | 6, dont Mobile Design à 49 sources |
| Structure, Navigation and Findability | 27 | 12, dont Information Architecture à 64 sources |

`stage3/check_playbooks.py` confirme les 6 à jour contre leurs concepts
(`sources_as_of` >= `updated` de chaque concept listé) et la couverture
complète des concepts de rang 1 de chaque thème. Prochaine dérive à surveiller
à la prochaine ingestion ou rédaction de concept touchant l'un de ces 55
concepts.
