# Ingestion 2026-09-10 — les 12 livres restants

Journal d'orchestration : pour chaque livre, les choix de découpage pris par
l'agent d'ingestion (short segments, `--absorb`, `--exclude`, `--relabel`,
options de conversion) et les corrections apportées par la relecture des
records contre le raw.

Ordre d'exécution : Laws of UX, Just Enough Research, UX Research, The Path to
Senior Product Designer, Product Management for UX People, User Story Mapping,
Storytelling in Design, Lean UX, INSPIRED, EMPOWERED, Lean Analytics, The Lean
Startup.

Baseline avant la série : 1067 records, 426 concepts, `verify_wiki.py` vert.

---

## 1. Laws of UX — Jon Yablonski, 2e éd.

Slug `laws-of-ux`, 14 chapitres, 14 records. EPUB natif, OPF correct : pas de
`--rejoin-lines`, `--strip-page-numbers`, `--relabel`, `--author` ni
`--published`.

**Découpage.** NCX imbriqué : 90 entrées pour 12 chapitres réels, chaque
`Overview` / `Origins` / `Examples` / `Conclusion` y étant listé. Le plan naïf
découpait 47 fragments.

- `--min-chars 1` : à 1500 par défaut, chaque ouverture de chapitre (588 c.)
  était fusionnée en avant et désroutait tous les `--absorb` en aval.
- Absorbés : les 4 sections de chacune des 10 lois ; les 4 morceaux de la
  préface (`Second Edition`, `Why I Wrote This Book`, `Who This Book Is For`,
  `What's in This Book`) ; les 4 sous-sections de `A Brief History of
  Psychology and Design` ; les 14 sous-sections des ch. 11 et 12.
- Gardé comme chapitre à part : `A Brief History of Psychology and Design`,
  seule entrée hors `^\d+\.` non absorbée, 7 576 c. de vraie matière que la
  préface aurait noyée.
- Exclus : `O'Reilly Online Learning`, `How to Contact Us` (appareil éditorial
  absent de `DEFAULT_EXCLUDE`) ; `Acknowledgments` et `Index` par défaut.

Aucun `[TABLE]` perdu, 235 691 c. extraits.

**Deux arbitrages hors runbook.** Les 5 lois à un seul record ne déclenchent
pas la création automatique de page : créées à la main (`Miller's Law`,
`Postel's Law`, `Von Restorff Effect`, `Tesler's Law`, `Doherty Threshold`),
chacune étant le sujet titre d'un chapitre entier ; elles restent `stub`. Les
10 lois entrent en rang 1 du thème `Psychology, Cognitive Load and Behaviour`
(10 → 20 concepts) parce qu'en rang 2 elles étaient tronquées par `MAX_RANK2`.

**Concepts.** 10 créés (5 par le fold, 5 à la main), 36 enrichis dont 7 pages
`developed` réécrites. Pas de nouveau thème. `check_playbooks.py` signale les
6 playbooks périmés : régénération non faite, notée dans `wiki/log.md`.

**Relecture.** 14 records relus contre le raw, **12 corrigés**, plus 13 pages
concept où le défaut s'était déjà propagé. Chiffres et citations en bloc :
exacts. Les erreurs sont toutes dans la paraphrase.

- Fabrications : Engelbart crédité de l'influence Papert/Piaget/Bruner qui ne
  vise que Kay ; Fitts et Chapanis « pionniers de l'ethnographie » là où le raw
  dit « une forme précoce de contextual inquiry » ; le scroll infini rangé sous
  le renforcement variable alors qu'il est sous « Infinite Loops ».
- Sens inversé : l'italien décrit comme langue « compacte » (le raw dit *less
  compact*) ; le groupe témoin du Peak-End décrit comme *higher-pain* ;
  « despite » pour « even ».
- Attributions : la loi de Fitts datée des crashs de la guerre (c'est
  l'origine des human factors, dans un encadré) ; loi de Tesler « formulée à
  PARC » (définie chez Apple) ; Privacy Checkup du ch. 10 recollé au ch. 12.
- Takeaways plaqués : « obligation éthique » pour « responsabilité », « speed
  directly enables flow », Smalltalk « applied psychological insights ».
- Citation tronquée hors bloc `>` : l'arbitrage même de la loi de Tesler
  (« by making the software a little more complex ») avait sauté.
- Concepts non traités retirés : `[[Visual Hierarchy]]` du ch. 7,
  `[[User Control]]` du ch. 11.
- Chiffres : Cowan 2001 présenté comme « recent research » ; dépression et
  solitude chez les jeunes adultes, pas les adolescents.

Faux positifs assumés : « 10 times more likely » (dérivé de *one-tenth as
likely*), `[[Information Architecture]]` sur Miller's Law, `[[Design
Consistency]]` sur l'effet esthétique-utilisabilité.

**À surveiller au livre suivant** : le contenu des encadrés. Presque toutes
les erreurs viennent de là, le stage 1 les fondant dans le corps du chapitre
au lieu de les traiter comme des digressions attribuées.

## 2. Just Enough Research — Erika Hall, A Book Apart, 2013

Slug `just-enough-research`, 11 chapitres, 11 records. EPUB natif A Book
Apart, NCX propre à 17 entrées, headings intacts, zéro `[TABLE]`. **Aucune
option de réparation** : ni `--rejoin-lines`, ni `--strip-page-numbers`, ni
`--relabel`, ni `--absorb`, ni `--min-chars` custom. `--author` et
`--published` forcés parce que l'OPF donne `2013-08`, que le script refuse.

**Découpage.**

- `Foreword` (1 933 c., dans SHORT SEGMENTS) : **accepté comme chapitre**. Il
  porte l'argument du livre, et c'est le premier segment du document, donc
  aucun chapitre précédent ne peut l'absorber. Précédent : le foreword de
  *Continuous Discovery Habits* est un record.
- `About A Book Apart` (361 c.) : **exclu**. Boilerplate éditeur, listé hors
  ordre spine, il se faisait absorber dans `Resources`.
- `Resources` (8 172 c.) : **exclu**. Annuaire d'outils de 2013 (Silverback,
  Morae, Snapz Pro, Skype) plus une liste de lectures.
- `References`, `Acknowledgements`, `Index`, `About the Author` : exclusions
  par défaut, rien à trancher.

**Piège de fusion évité.** `Organizational Structure` est à la fois un alias
d'`Organizational Culture` dans le corpus et une clé `BOOK_MERGES` pointant
sur `Studio Structure` depuis les livres studio ; un dict n'a qu'une valeur
par clé. Le record du ch. 4 a été édité à la main pour citer
`Organizational Culture` directement, sans toucher à l'alias des livres
studio. Non-reproductibilité documentée dans `merge_map.py`.

**Concepts.** 2 créés (`Task Analysis`, `Competitive Analysis`, tous deux
`stub`), 23 enrichis, 0 nouveau `developed` (un livre = un ouvrage). Thèmes
`Choosing and Running Research` et `Research Rigour and Ethics`, pas de
nouveau thème. Convergence des candidats quasi parfaite : 25 noms pour 11
chapitres, 17 pointant déjà sur une page existante.

**Relecture.** `check_claims.py` : 0 hit, et c'est précisément le piège. Les
dérives de ce livre sont hors de portée d'un script qui cherche des chiffres.
L'ingestion en avait corrigé 4 à la main (sept questions d'audit et non six,
mint.com « it's arguable », les cinq composantes attribuées à Nielsen, une
négation inversée en conclusion : les quatre vérifiées en place). La
relecture fraîche en a trouvé **30 de plus, sur 10 records des 11**.

- **Modalisateurs effacés**, la moitié des corrections : « one way to know »
  devenu « how to know » ; « very possible » devenu « will » ; « potentially
  useless » devenu « useless » ; « often an indicator » devenu « signals » ;
  « at least two or three, ideally » devenu « requires two or three ».
- **Fuites entre chapitres** : les trois actes de l'entretien (ch. 5) mis au
  ch. 3 ; la liste des bons participants (ch. 3) mise au ch. 5. Aucune gate ne
  peut voir ça, l'affirmation étant vraie ailleurs dans le livre.
- **Attributions perdues** : citation de Paul Ford donnée sans auteur ; SWOT
  sans Albert Humphrey ; le maximum local sans Andrew Chen ; le diagramme de
  modèle mental sans Indi Young.
- **Comparateur aplati** : le livre hiérarchise « deuxième plus cher » (test
  repoussé) et « plus cher de tous » (test fait par les clients après
  lancement), le record en faisait un « ou ».
- **Claims réécrits vers le vertueux** : « you either care about usability, or
  you're a jerk » devenu « or do not claim to be user-centered » ; « the
  greatest danger is that they will not be able to sit idly by » devenu « the
  designer should avoid facilitating ».

**À surveiller au livre suivant** : les modalisateurs et les fuites entre
chapitres.

## 3. UX Research — Brad Nunnally et David Farkas, O'Reilly, 2016

Slug `ux-research`, 16 records (foreword + 15 chapitres). EPUB Calibre né d'un
PDF (`pdftohtml`). `--author` et `--published` forcés : l'OPF donne
`2019-08-26`, date de génération du PDF, alors que la page de copyright dit
« November 2016: First Edition / 2016-11-04: First Release ».

**Le NCX est inutilisable, premier cas du corpus.** 4 `navPoint` (`Foreword`,
`PART I`, `PART II`, `PART IV`, dans le désordre du `playOrder`) pour un livre
de 15 chapitres, aucun ne pointant sur un chapitre. `fetch_epub.py` ne coupe
que sur le NCX : le plan naïf donnait 3 fichiers dont un de 360 262 caractères
couvrant les chapitres 13 à 15, et **rien ne l'avertissait** — toutes les
entrées étaient traitées, aucun segment n'était court. NCX reconstruit à la
main dans un EPUB de travail au scratchpad (l'original ne bouge pas) :
23 entrées ancrées sur les marqueurs d'ouverture que le livre porte déjà,
`<a id="pNN">` devant les lignes `[ 1 ]` ... `[ 15 ]`, `[ Part I ]` ...
`[ Part IV ]`, `[ Foreword ]`, `[ Preface ]`, `[ Index ]`,
`[ About the Authors ]`. Le champ `extraction` des 16 raw porte la réparation.

**Découpage.** Options : `--rejoin-lines`, `--min-chars 2000`,
`--exclude '^Preface$'`.

- 4 ouvertures de partie (205, 1 623, 1 661, 1 545 c.) dans SHORT SEGMENTS :
  **fusion en avant acceptée**, obtenue en montant `--min-chars` à 2000 plutôt
  qu'avec `--absorb`, qui les aurait recollées au chapitre **précédent**. À
  1500 (défaut), trois d'entre elles devenaient des records d'une page et demie.
- `Preface` (10 309 c.) : **exclue**. Sommaire en prose chapitre par chapitre
  + encart O'Reilly Safari + « How to Contact Us » + remerciements. Un record
  là-dessus est une invitation à la fuite entre chapitres.
- `Foreword` (5 471 c., Steve Portigal) : **gardée** comme chapitre, elle porte
  l'argument du livre. Précédents *Just Enough Research* et *Continuous
  Discovery Habits*.
- `Index` (21 040 c.) et `About the Authors` (874 c.) : exclusions par défaut.

Aucun `[TABLE]` perdu, 323 763 c. extraits — mais `pdftohtml` avait déjà aplati
les tableaux en lignes entremêlées avant pandoc, ce qui est la vraie limite du
fichier et a été signalé aux agents (Table 3-1 et 4-1 notamment).

**Concepts.** 33 des 38 noms candidats pointaient déjà sur une page existante.
7 entrées `BOOK_MERGES`. 2 pages créées (`Debrief Session`,
`Nonverbal Communication`, stubs), 33 enrichies, prose rafraîchie sur 16.
`Active Listening` passe `developed` (9 records, 2 ouvrages), placée dans deux
thèmes. `[[Improvisation]]` laissé pendant (un seul record). Pas de nouveau
thème.

**Relecture.** `check_records.py` et `check_claims.py` verts avant comme après.
Relecture des 16 records contre le raw : **22 corrections sur 12 records**.

- **Attributions perdues (7), défaut n°1 de ce livre.** Chacun des
  15 chapitres contient un encadré d'interview « Voice from the Streets » avec
  un praticien nommé, et trois records en citaient le texte comme s'il venait
  des auteurs (Dan Brown, Ofer Deshe, Kyle Soucy). Quatre autres présentaient
  une lecture conseillée (« for more information, see *Gamestorming* ») comme
  la source de l'affirmation.
- **Modalisateurs effacés (6)** : « we recommend two separate research tracks »
  devenu une règle ; « at least three to four days before » devenu « 3-4 days
  before » ; « assuming participant availability is not an issue, three to five
  users per group » devenu un chiffre absolu (deux fois, dont dans une
  citation) ; « it is very difficult... at the same time » devenu impossible ;
  « a common way of doing this » devenu « researchers should ».
- **Fabrications (4)** : « two copies required » des formulaires de consentement,
  A/B testing rangé sous les méthodes *generative* (le label ne pouvait venir
  que du tableau 3-1 aplati), l'encadré Abby Covert présenté comme une
  démonstration d'affinity diagramming, « preventing siloing of findings ».
- **Fuites entre chapitres (3)** : les sections « When and Where » du ch. 4
  recopiées dans le record du ch. 5, « tangible, measurable outcomes » du ch. 3
  importé au ch. 5, une idée du ch. 14 dans le ch. 15.
- **Réécritures vers le vertueux (3)** : « psychological safety » pour
  « comfort and trust », « compensating participants fairly » pour un honoraire
  décrit de façon purement pratique, « responsabilité de protéger » pour « an
  easy way to alleviate any concerns ».
- Concepts retirés : `[[Mental Model]]` du ch. 13 (c'est le ch. 14),
  `[[Improvisation]]` du ch. 8 (simple annonce du ch. 10). Une citation du
  ch. 1 remplacée : verbatim mais portant la césure « dis-ruptors ».

**Ajout au script.** `fetch_epub.py` avertit désormais quand un chapitre du
plan dépasse 60 000 c. **et** quatre fois la médiane : c'est le symptôme
observable d'un NCX qui liste des parties au lieu de chapitres. Vérifié : se
déclenche sur l'EPUB d'origine de ce livre, silencieux sur le NCX reconstruit,
sur *Just Enough Research* et sur *Solving Product Design Exercises*.

**À surveiller au livre suivant** : les encadrés attribués, encore. Deux livres
de suite, c'est la zone la plus coûteuse, et c'est celle qu'aucune gate ne voit.

**Second ajout au script.** `stage3/generate_themes.py` était non déterministe :
`counter.most_common(2)` départage une égalité par ordre d'insertion, issu d'un
`glob()` sur `wiki/episodes`, donc de l'ordre du système de fichiers. Un concept
à égalité entre deux thèmes changeait de thème à chaque exécution, et deux
lancements de suite réécrivaient les 22 fichiers de thème avec des « Sharp
edges » différentes — du bruit pur dans chaque commit d'ingestion depuis le
début. Égalité départagée par nom de thème, idempotence vérifiée par deux runs
consécutifs.

## 3. UX Research — Brad Nunnally et David Farkas, O'Reilly, 2016

Slug `ux-research`, 16 records (foreword de Steve Portigal + 15 chapitres),
323 763 c. EPUB né d'un PDF.

**Le NCX mentait par omission.** 4 `navPoint` (`Foreword`, `PART I`, `PART
II`, `PART IV`) pour un livre de 15 chapitres, aucun ne pointant sur un
chapitre. Comme `fetch_epub.py` ne coupe que sur le NCX, le plan naïf donnait
3 fichiers dont un de 360 262 c. **NCX reconstruit à la main** dans un EPUB de
travail au scratchpad (l'original ne bouge pas), 23 entrées ancrées sur les
marqueurs d'ouverture que le livre porte déjà (`<a id="pNN">` devant `[ 1 ]`
… `[ 15 ]`, `[ Part I ]` … `[ Part IV ]`). Le champ `extraction` des 16 raw
porte la réparation : sans ça la provenance serait fausse, rejouer la commande
contre l'EPUB d'origine ne reproduisant pas les fichiers.

**Découpage.**

- Les 4 ouvertures de partie (205 à 1 661 c.) : fusion en avant acceptée, elles
  appartiennent au chapitre qui suit.
- `--min-chars 2000` plutôt qu'un `--absorb` pour ces ouvertures : `--absorb`
  les aurait recollées au chapitre **précédent**, et à 1500 trois d'entre elles
  devenaient des records d'une page et demie.
- `Preface` (10 309 c.) : **exclue**. Sommaire en prose chapitre par chapitre,
  encart O'Reilly Safari, « How to Contact Us », remerciements. Un record
  là-dessus est une invitation à la fuite entre chapitres.
- `Foreword` (5 471 c., Steve Portigal) : gardé comme chapitre.
- `--rejoin-lines` obligatoire (un `<p>` par ligne). Ni `--strip-page-numbers`
  ni `--relabel` : les libellés reconstruits sont propres.

**Concepts.** 38 candidats dont **33 pointaient déjà sur une page existante**,
un seul nom coiné hors liste. 2 créés (`Debrief Session`,
`Nonverbal Communication`), 33 enrichis. **1 passage en `developed` grâce au
deuxième ouvrage, et c'était le but** : `Active Listening`, 9 records, 2
ouvrages, `stub` depuis *Articulating Design Decisions*. Thèmes `Choosing and
Running Research` et `Influence, Stakeholders and UX Maturity`, pas de nouveau
thème. Un désaccord entre sources explicité dans `Bias in Research` : ce livre
admet qu'un chercheur expérimenté casse volontairement ses propres règles.

**Deux scripts corrigés au passage.** `fetch_epub.py` avertit maintenant quand
un chapitre du plan dépasse 60 000 c. **et** quatre fois la médiane (le
garde-fou existant ne visait que le NCX trop riche, pas le NCX trop pauvre).
Et `generate_themes.py` n'était pas déterministe : l'égalité de
`most_common(2)` est désormais départagée par nom de thème, ce qui supprime 22
fichiers de churn à chaque ingestion.

**Relecture.** `check_claims.py` : 0 hit, encore. L'ingestion avait déjà
corrigé 22 défauts à la main (7 attributions, 6 modalisateurs, 4 fabrications,
3 fuites, 3 réécritures vertueuses) ; sondage de la relecture : tous en place.
La relecture fraîche en a trouvé **21 de plus, sur 10 records des 16**.

- **Épigraphes de chapitre**, le défaut résiduel de ce livre : la citation de
  George Bernard Shaw (« the illusion that it has taken place ») rangée dans
  `## Quotes` comme une phrase des auteurs ; l'épigraphe de Daniel Goleman
  devenue la définition maison des soft skills du ch. 11. Elles n'ont pas la
  forme d'un encadré signé, donc elles se glissent dans la voix du chapitre.
- Attribution : un item entier du ch. 9 venant de l'encadré Voice from the
  Streets de Lis Hubert, présenté comme le propos du chapitre.
- Modalisateurs : « assuming correct tagging on the backend » effacé ; « while
  not required, this form is a courtesy » devenu « will » ; « often surveys »
  devenu « should be » ; « a common severity scale » devenu « the NN/g
  standard approach » ; « the interpretation of expressions is universal »
  affaibli en « largely universal », dérive dans l'autre sens.
- Fabrications : quatre « biais » là où le raw dit « factors » et où deux
  seulement sont des biais ; « narrative arc » absent du ch. 14 ; le jeu
  « Yes, And… » compté comme une des dix règles d'improvisation ; l'empathie
  prêtée au foreword de Portigal, qui ne l'emploie jamais.
- Fuite : « Part II introduces quantitative research methods as foundational »
  au ch. 3, alors que Part II est « Planning and Preparation ».
- Réécritures vertueuses : « consent forms » devenu « informed consent » ;
  « putting your participant at ease » devenu « signal that you respect the
  participant's space » ; la neutralité du chercheur devenue « so the
  participant feels safe ».
- Un record sans titre H1, contraire au template de `SCHEMA.md`.

Faux positifs assumés : « tree jacking » est bien dans le livre ; les échelles
de sévérité et les blocs horaires ressemblaient à des tableaux aplatis mais
sont en prose. Aucun record n'affirme le contenu des tables 3-1 et 4-1,
illisibles dans le raw.

**À surveiller au livre suivant** : les épigraphes de chapitre.

## 4. The Path to Senior Product Designer — Artiom Dashinsky, 2023

Slug `path-to-senior-product-designer`, 25 chapitres, 25 records. Métadonnées
toutes lues dans l'OPF, aucune forcée : l'EPUB vient de Pages Publishing macOS,
pas de Calibre, donc pas de hash ni d'`Unknown`. Auteur vérifié contre la page
de titre. URL `productdesigninterview.com`, déjà celle du précédent livre de
Dashinsky au corpus.

**Découpage.** NCX plat, 30 entrées, aucune sous-entrée, aucun avertissement de
chapitre hors-norme (48 k c. au plus gros pour une médiane de 15 k). Aucune des
deux pathologies de NCX rencontrées jusqu'ici.

- `Footnotes` (10 016 c.) : **exclu**. Liste d'URL nue, zéro prose.
- Les 4 titres de partie (34 à 37 c.) : fusion en avant acceptée, ils
  alimentent le champ `part` du chapitre suivant.
- `Final thoughts` (1 507 c.) : gardé comme chapitre, juste au-dessus de
  `--min-chars`.
- Aucune autre option : EPUB natif, prose continue, césures propres, libellés
  corrects.

**Concepts.** 7 créés (`Career Growth Plan`, `Design Competencies`,
`Career Ladder`, `Design Advocacy`, `Design Ownership`, `Mentorship`,
`Promotion`), 14 enrichis, **4 passages en `developed`** (`Design Advocacy`,
`Design Strategy`, `Performance Review`, `Productivity`). 4 thèmes touchés,
aucun nouveau, aucun playbook. Le livre ne contient aucune épigraphe (zéro
blockquote dans les 25 raw) : le défaut n°1 du livre précédent était sans
objet.

**Relecture.** `check_claims.py` : 0 hit, quatrième fois de suite. L'ingestion
avait corrigé 10 défauts à la main (dont les 25 % d'évaluation attribués à Mike
Davidson chez Twitter, une stat Gallup dépouillée de sa source, quatre
décomptes de listes faux) : tous vérifiés en place, et le balayage complet des
16 autres décomptes écrits en lettres est propre. La relecture fraîche a trouvé
**19 défauts de plus, sur 17 records des 25**.

- **Deux résumés qui affirment l'inverse du chapitre**, en le « rationalisant » :
  la technique décrite comme « may be less powerful » quand il existe une
  équipe design ops devenue « the skill extends to strategic thinking » ; les
  avis négatifs à chercher **sur les concurrents** devenus « to fix your own
  problems ». C'est le seul défaut qui rend un record faux plutôt
  qu'incomplet.
- **Généralisations du « je » de l'auteur** : « at Dropbox, impact consists of
  three factors » devenu une règle ; « I mapped out the minimum requirements
  based on my experience » devenu « presents a competency framework » ; « how
  I structure my interviews » devenu « a typical interview » ; « the biggest
  impact on my growth » devenu « one of the highest-impact growth activities ».
- **Attributions perdues** : Joel Califa, Shaan Puri (ABZ), *Giftology* de John
  Ruhlin, Paul Graham (*Maker's Schedule, Manager's Schedule*), un template
  gratuit NN/g, EDIP « used by extreme sports and military instructors », le
  5W1H adapté du premier livre de l'auteur.
- **Fuites entre chapitres** : les libellés de la Figure 4.3 collés à la
  Figure 3.2 (une note 1 à 5) ; la matrice d'Eisenhower du ch. 16 mélangée à la
  matrice stakeholder du ch. 14 ; une phrase de *Getting Promoted* recopiée au
  ch. 21, qui dit l'inverse.
- Chiffres déplacés : 10 % de chances « d'être promu » là où le raw dit
  « d'obtenir le poste » ; « thousands of designers at MAANG » là où le raw dit
  « tens of thousands, companies of all sizes, including MAANG ».

Faux positifs assumés : « seven steps » pour un cadre qui n'en liste que cinq
est **dans le raw** (la figure porte les deux manquants), on ne corrige pas
vers le vertueux. `[[Design Leadership]]` et `[[Design Presentation]]`
retirés puis rétablis : la page `developed` construit une lecture inter-sources
défendable, ce n'est pas une fabrication du record.

**À surveiller au livre suivant** : la phrase qui améliore le chapitre, un
modalisateur restrictif du raw (« may be less powerful », « from my
experience », « at mature companies ») transformé en règle positive.

## 5. Product Management for UX People — Christian Crumlish, Rosenfeld Media, 2022

Slug `product-management-for-ux-people`, 14 records (FAQ + foreword +
introduction + 11 chapitres). EPUB natif : ni `--rejoin-lines`, ni `--author`,
ni `--relabel`.

**Ingestion interrompue en cours de route** par une limite de dépense, après
l'étape 2 et le pilote de 3 records. Reprise par un agent frais à l'étape 3 :
le champ `extraction` des raw a suffi à restituer les décisions de découpage,
ce qui valide la résumabilité annoncée par le skill.

**Découpage.** NCX imbriqué, chaque sous-section ayant son entrée. La décision
structurante est `--absorb '^(?!CHAPTER \d+:|Foreword|Introduction|Frequently
Asked Questions)'` en lookahead négatif : sans lui le plan explosait en
dizaines de fragments. Avec `--min-chars 1`, même raison que pour Laws of UX.
Exclus : `How to Use This Book`, `Footnotes`.

**Le chapitre d'interviews de fin d'ouvrage n'existe pas dans ce livre**,
contrairement à l'habitude Rosenfeld : les voix de praticiens sont réparties
dans les chapitres, en encadrés `FROM THE TRENCHES` (une quinzaine),
`A DAY IN THE LIFE OF A ... PM` (sept) et `UX SUPERPOWER ALERT`. L'absorb les
garde avec leur chapitre, ce qui est le bon sort : chacune est un témoignage
sur le sujet de son chapitre, pas un appendice autonome.

**Le pilote passait les deux gates au vert et était faux.** Zéro attribution
(ni Zaveri, ni Pagels-Minor, ni LeMay, ni Cagan, ni Mironov, ni Cutler…) et un
décompte faux en lettres. Les trois records ont été réécrits, et c'est ce qui a
produit les consignes de la vague : typologie explicite des encadrés Rosenfeld
avec la règle « une boîte utilisée = son nom cité », et l'ordre de compter les
puces du raw avant d'écrire un nombre.

**Concepts.** **0 créé**, 33 enrichis, 21 pages `developed` rafraîchies par
intégration jamais par réécriture, **2 passages en `developed`**
(`Product Management`, 9 records et 4 ouvrages ; `Assumption Testing`).
Fusion quasi vide comme voulu : 34 candidats, 33 déjà des pages, une seule
coinage. 3 thèmes touchés, aucun nouveau.

**Relecture.** `check_claims.py` : 0 hit, cinquième fois. L'ingestion avait
corrigé 9 défauts à la main, tous des noms disparus ou des réserves effacées.
La relecture fraîche en a trouvé **24 de plus, sur 10 records des 14**.

- **Attributions perdues dans les encadrés en incise** : la citation de Matt
  LeMay posée sans nom dans `## Quotes` ; le pretotype sans Alberto Savoia ; le
  holdover sans Ryan Rumsey ; la décohérence sans Dawn Russell ; le partenariat
  avec les équipes clients sans Craig Newmark. Une attribution carrément
  inversée : « chief information architect » rendu à Jorge Arango alors que le
  titre est de Crumlish.
- **Désaccords escamotés**, spécialité de ce livre : Caio B. Nishihara veut
  sortir le design de la ligne produit quand il est un driver stratégique, le
  record n'en disait rien ; Matt LeMay voit « des PM tomber amoureux du non »,
  le chapitre 10 n'en gardait rien.
- **Réserves effacées** : « Kinda » devenu « need not conflict » ; « for some
  reason, there is a consensus » devenu un consensus ; le risque de frustrer
  les utilisateurs d'une fake door supprimé ; « it's not that any of these
  tasks must be owned by one role » supprimé.
- **Décomptes faux sur listes longues** : « twelve named methods » pour 13
  items, « eight common models » pour 9 puces.
- **Une sur-correction de l'ingestion, retournée contre elle-même** : voulant
  réparer la règle inventée des 2 000 utilisateurs par bucket, elle avait écrit
  que Crumlish ne donne aucune règle de taille d'échantillon, alors que le raw
  l'énonce noir sur blanc comme « a very broad rule of thumb ». Corrigé dans le
  record et dans deux pages concept.

**À surveiller au livre suivant** : les listes à puces de plus de six items, et
les corrections de l'ingestion elle-même, qui peuvent dépasser la cible.

## 6. User Story Mapping — Jeff Patton avec Peter Economy, O'Reilly, 2014

Slug `user-story-mapping`, 23 records (3 forewords de Martin Fowler, Alan
Cooper et Marty Cagan + Preface + Read This First + 18 chapitres). EPUB natif :
ni `--rejoin-lines`, ni `--strip-page-numbers`, ni `--relabel`. `--published`
pris dans `dcterms:modified`, `dc:date` ne donnant que `2014` que le script
refuse. `--author` forcé, l'OPF ne déclarant que Patton.

**Découpage : 23 chapitres sur 213 entrées NCX.** NCX imbriqué, un fichier HTML
par chapitre, ses sous-sections en enfants. Le plan naïf donnait 108 fragments.

- `--absorb` en lookahead négatif **énumérant les 23 titres exacts**, pas un
  motif de forme : les chapitres 5, 6 et 14 ont des sous-sections elles-mêmes
  numérotées (« 1. Card », « 2. Conversation ») qu'un `^\d+\.` aurait promues
  en chapitres.
- `--min-chars 1`, indispensable : plusieurs ouvreurs de chapitre font moins de
  1 000 c. (« 16. Refine, Define, and Build » : 188 c.) et partaient en avant
  **avant** d'avoir pu absorber leurs propres sous-sections, ce qui fusionnait
  deux chapitres et désalignait tous les absorbs suivants.
- Exclus, absents de `DEFAULT_EXCLUDE` : la page de titre `User Story Mapping`
  (le titre du livre ressemble à un chapitre), `Safari® Books Online`,
  `How to Contact Us`, `Colophon`.
- `The End, or Is It?` (1 430 c.) absorbé dans le ch. 18. Les 3 forewords
  invités gardés comme records à part entière.

**Concepts.** 7 créés (`Story Mapping`, `User Story`, `Shared Understanding`,
`Product Backlog`, `Story Slicing`, `Validated Learning`, `Release Planning`),
23 enrichis dont 19 pages `developed` rafraîchies, **3 passages en
`developed`** (`Story Mapping`, `Product Outcome`, `Product Trio`). 3 thèmes
touchés, aucun nouveau. Deux alias volontairement non posés : `User Stories`
(un record NNG déjà `processed` y met un autre sens, une histoire racontée sur
les utilisateurs et non une unité de livraison) et `Backlog Management`.

**Relecture.** `check_claims.py` : 1 hit, tranché (« the 1980s arcade game
Asteroids » là où le raw ne dit que « an early video game called Asteroids »).
L'ingestion avait corrigé 5 défauts à la main. La relecture fraîche en a trouvé
**39 de plus, sur 20 records des 23** : le pire ratio de la série, et le livre
le plus exposé, Patton fonctionnant entièrement par histoires signées.

- **Neuf encadrés contribués intégralement absents des records** : Ceedee
  Doyle (Assurity), Rick Cusick (Reading Plus), Andrea Schmieden (SAP), Mat
  Cropper (ThoughtWorks), Ben Crothers (Atlassian), Erin Beierwaltes et Aaron
  White, Josh Seiden et Demian Repucci, Nicola Adams et Steve Barrett (RAC
  Insurance), Chris Gansen et Jason Kunesh (Obama Campaign Dashboard 2012).
  Aucune gate ne voit qu'une contribution nommée a disparu.
- **Généalogies effacées** : le walking skeleton d'Alistair Cockburn, le
  What-About de David Hussman, les template zombies de DeMarco, le template
  Connextra via Rachel Davies, le MVP de Frank Robinson avant Ries, le design
  thinking d'IDEO puis Stanford, Steve Blank avant Ries, valuable-usable-feasible
  de Cagan, le « half a baked cake » de Luke Hohman, les orgzonas de Lane
  Halley, Osterwalder **et Pigneur**.
- **Confusion de personnes** : la boucle build-measure-learn attribuée à
  « Eric », le PO de Liquidnet, au lieu d'Eric Ries.
- **Modalisateur écrasé, le plus grave** : « my belief, not rooted in any
  formal scientific research or studies » présenté comme « Patton cites
  research showing that 20 percent of features are successful ».
- **Fuites entre chapitres** : le template Connextra (ch. 7) au ch. 6 ; les
  asteroids (ch. 17) au ch. 16 ; la séparation des revues (ch. 18) au ch. 16.
- **Paroles de chanson** : une citation des Rolling Stones en bloc `>`,
  remplacée par une phrase de Patton.
- **Décompte faux** : les trois amigos recomptés (développeur substitué au
  membre de l'équipe discovery).
- **Deux corrections de l'ingestion allées trop loin** : « a term Patton
  borrows from the 1986 comedy » alors que Patton dit ignorer qui a inventé le
  nom, et « arcade game » resté dans la correction Asteroids.

**À surveiller au livre suivant** : les encadrés signés purement ignorés, et la
correction qui dépasse sa cible.

## 7. Storytelling in Design — Anna Dahlström, O'Reilly, 2019

Slug `storytelling-in-design`, 15 records (préface + 14 chapitres).
Métadonnées toutes issues de l'OPF. 37 Mo d'EPUB, aucun résidu d'image dans le
raw, aucun `[TABLE]`.

**Découpage.** NCX imbriqué, 118 entrées pour 14 parents.

- `[ Index ]` (47 723 c.) : exclu. Ses crochets l'empêchaient de matcher
  `^index\b` de `DEFAULT_EXCLUDE`.
- `[ Preface ]` (24 188 c.) : gardé comme chapitre, c'est du vrai contenu.
- Les 14 ouvreurs « Chapter N. » (81 à 161 c.) : gardés comme chapitres grâce à
  `--min-chars 1` ; au défaut ils partaient en avant et fusionnaient deux
  chapitres.
- Les 102 sous-sections, dont les 9 SHORT SEGMENTS restants : absorbées.
- **Contrairement au livre précédent, l'énumération des titres exacts n'a pas
  été nécessaire** : tous les ouvreurs sont libellés « Chapter N. » et aucune
  sous-section ne commence par ce mot, donc `^(?!chapter \d+\.|\[)` suffit, le
  `\[` protégeant `[ Preface ]`. C'est le libellé des ouvreurs qui décide, pas
  la forme du NCX.

**Concepts.** 7 créés (`Narrative Structure`, `Experience Shape`,
`Red Thread`, `Scene Structure`, `Character Development`,
`Nonlinear Storytelling`, `Subplot`), 23 enrichis, **3 passages en
`developed`** (`Shared Understanding`, `User Flow`, `Wireframing`). 2 thèmes
touchés, aucun nouveau.

**Première utilisation de `check_names.py`**, écrite juste avant ce livre : 37
hits côté ingestion, dont ~12 vraies attributions manquantes ; 28 hits côté
relecture, dont 2 vraies. Rendement réel autour de 7 à 30 % selon la passe,
sous le tiers annoncé par sa calibration. Verdict de la relecture : elle voit
le nom présent dans le raw et absent du record, pas le cas dominant ici, qui
est **le nom absent des deux mais dont la phrase est reprise**. Peu coûteuse à
trancher, elle ne remplace pas la lecture. Bruit bien typé et reconnaissable en
une ligne : acronymes pris pour des noms (CMO, CTA, SVP), personnages de
fiction, légendes de figures, pays, notes de bas de page.

**Relecture.** L'ingestion avait corrigé une douzaine d'attributions et deux
chiffres fabriqués (« 400 hours of content every hour », « 3.7 million
broadcasters », absents du raw). Toutes en place, aucune allée trop loin. La
relecture fraîche a trouvé **57 corrections, sur les 15 records**, le plus gros
volume de la série.

- **Citations tierces non créditées dans `## Quotes`**, le défaut propre à ce
  livre et qu'aucune gate ne voit : 43 blocs `>` dans les 15 records, **11 ne
  sont pas de Dahlström**, 6 étaient posés nus. Wilson Miner, Cristos Goodrow
  (VP engineering YouTube), Meg Dickey-Kurdziolek, Samo Zakkir, Brandon Chu,
  Ami Ben David. `check_records.py` les valide puisqu'elles sont verbatim.
- **Positions de l'autrice retournées vers ce qui sonne raisonnable**, le
  défaut le plus coûteux : « I'm all for using Lorem ipsum when used in
  conjunction with notes » devenu une mise en garde contre le placeholder ;
  « aesthetically pleasing design alone won't be enough » devenu « not luxury,
  it is essential in stressful contexts » ; un arbitrage tranché présenté comme
  non tranché.
- **Décomptes faux** : six patterns de Vonnegut pour huit, huit émotions
  virales pour dix, sept approches du *Writer's Digest* réduites à trois sans le
  dire, « Aristotle's seven golden rules » pour quatre éléments « inspired by ».
- **Connaissance externe fabriquée** : une durée de 2-3 minutes par page
  produit mise entre guillemets alors que le livre ne donne aucun chiffre ; une
  liste d'étapes du ch. 5 recopiée au ch. 9 ; le contenu d'une figure absente du
  raw.
- **22 attributions perdues hors citations**, dont Don Norman, Alan Cooper,
  Nancy Duarte, Chris Risdon, Aarron Walter, et la généalogie du *röd tråd*.
- **8 modalisateurs et « je » restaurés**, **4 contrepoints escamotés**,
  **6 fuites entre chapitres**, **5 concepts retirés du frontmatter** dont trois
  s'auto-dénonçaient (« While not explicitly named »).

**À surveiller au livre suivant** : le glissement de modalité plus que
l'attribution nominale. Les trois défauts les plus coûteux ici ne sont pas des
noms perdus mais des positions de l'autrice retournées vers ce qui sonne
raisonnable, et aucune gate ne peut les voir.

**Dette de script identifiée** : `check_claims.py` ne voit pas les nombres
décimaux (« 3.7 million » fabriqué est passé alors que « 400 » de la même
phrase a été signalé). Étendre sa regex aux décimaux et aux suffixes.
