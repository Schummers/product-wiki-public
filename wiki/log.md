# Journal de bord

## 2026-07-30 migration | Design wiki -> product-wiki
* Domaine renommé `product-wiki/`, nested repo GitHub (voir `CLAUDE.md`).
* 90 fiches migrées vers le schéma étendu (`SCHEMA.md`, ADR 0001) : frontmatter canonique + `published`, `concepts`, `raw`.
* Couche concepts normalisée : 253 stubs français -> 231 concepts anglais dédoublonnés avec frontmatter et aliases (ADR 0002). Toutes les fiches concepts sont des stubs : la définition et la pratique restent à écrire (étape 2).
* `#` retiré des noms de fichiers (cassait les wikilinks Obsidian), 318 fichiers réécrits.
* `index.md` régénéré, intégrité vérifiée (`verify_wiki.py` OK).

## 2026-07-31 étape 2 | couche concepts

* **Fusion.** 1666 noms de concepts candidats proposés par l'étape 1 réduits à 1235 : carte curée `stage2/merge_map.py` (290 règles) + `stage2/singleton_map.py` (148 absorptions de singletons revues à la main). 653 fiches réécrites (frontmatter `concepts:` et wikilinks du corps). Variantes typographiques rattrapées ensuite (Ecommerce, Creative Problem-Solving) et accents précomposés corrigés sur 2 liens.
* **Pages.** 384 pages concept générées par `stage2/generate_stubs.py` : frontmatter, aliases hérités de la fusion, `## Sources` construite depuis les bullets `## Concepts` des fiches. 26 stubs vides dont le nom était devenu un alias ont été supprimés.
* **Rédaction.** Les 147 concepts à 5 sources ou plus ont reçu `## Definition` et `## Practice` (2,2 Mo, 15 Ko par page en moyenne), écrits à partir des seules fiches, jamais du raw. Les désaccords entre sources sont signalés, pas arbitrés. 237 concepts à 2-4 sources restent `stub`. Les concepts cités par une seule fiche n'ont pas de page : leurs wikilinks sont des liens cassés assumés.
* **Correctifs corpus.** 15 fiches du lot 056 de l'étape 1 contenaient du texte template (« Key point 1 — summary from article », bullets `## Concepts` non rédigés) ; réparées depuis leur raw sans toucher aux concepts fusionnés. Les 5 pages écrites avant cette réparation ont été enrichies après coup.
* Fiches passées en `status: processed`. `index.md` régénéré.

## 2026-08-21 étape 3 | couche thème, routeur, playbooks

* **Constat de départ.** Le corpus répondait déjà aux questions posées (les 147
  concepts `developed` font 3000 à 6000 mots, sourcés), mais rien ne routait une
  question vers la bonne page : le seul index faisait 220 Ko à plat. Le manque
  était l'accès, pas le contenu. Décision et alternatives dans `docs/adr/0003`.
* **Thèmes.** 21 thèmes générés depuis `stage3/theme_map.py` (curation, seedée
  par un clustering de co-occurrence sur 1240 paires de concepts) et
  `stage3/theme_prose.py` (jugement : 21 déclencheurs, 147 gloses adossées aux
  sous-titres réels des pages). Les 147 concepts `developed` sont placés, 32
  dans deux thèmes. `_router.md` fait 594 mots.
* **Rang 2.** Les stubs et les concepts à source unique sont rattachés aux
  thèmes via les records partagés, sans curation : une ingestion les reclasse
  seule. 1505 rattachements. C'est ce qui rend enfin joignables des idées
  étroites et actionnables (`Toggle Switch`, `Alt Text`, `Button Design`).
* **Orphelins.** `wiki/orphans.md` indexe les 848 concepts à source unique sans
  page, chacun vers son record. Leurs wikilinks n'étaient que des impasses.
* **Gate réparé.** `verify_wiki.py` signalait 1701 problèmes, dont 1700 étaient
  les liens cassés assumés : un gate rouge en permanence n'attrape aucune
  régression. Règle ajoutée : un nom cité par 1 record sans page est normal, par
  2+ c'est un manque. Passé à 0. Deux vrais défauts trouvés dessous et corrigés
  (`Creative Problem Solving` absorbé en alias d'`Ideation`, backlink `E-Commerce`
  manquant vers `2020-11-08_augmented-reality-useful`).
* **Playbooks.** Nouveau type, règles cochables pour une revue de design, sur 6
  thèmes seulement (`docs/adr/0004`). Les 6 écrits, 145 règles au total, chacune
  distillée d'une lecture intégrale des pages concept sources (pas d'un résumé) :
  Usability Heuristics and Evaluation (18), Accessibility and Inclusion (20),
  Page Composition and Hierarchy (20), Interaction and Interface Patterns (35),
  Mobile and Multi-Device (25), Structure Navigation and Findability (27).
  `stage3/check_playbooks.py` surveille leur dérive contre les pages concept et
  passe au vert sur les 6.
* **Skills.** `product-wiki-consult` et `product-wiki-review` dans
  `system/skills/product-wiki/`, symlinkés et gitignorés.

## 2026-09-10 pipeline livre | UX Research (Brad Nunnally et David Farkas)

* **Stage 0.** EPUB Calibre né d'un PDF (`pdftohtml`), et le premier du corpus
  dont le NCX est **inutilisable** : 4 `navPoint` (`Foreword`, `PART I`,
  `PART II`, `PART IV`) pour un livre de 15 chapitres, aucun ne pointant sur un
  chapitre. `fetch_epub.py` ne coupe que sur le NCX, donc le plan naïf donnait
  3 fichiers dont un de 360 000 caractères. Le NCX a été **reconstruit à la
  main** avant le run, dans un EPUB de travail au scratchpad (l'original ne
  bouge pas) : 23 entrées ancrées sur les marqueurs d'ouverture de chapitre du
  livre lui-même (`<a id="pNN">` devant les lignes `[ 1 ]` ... `[ 15 ]`,
  `[ Part I ]`, `[ Foreword ]`, `[ Index ]`, `[ About the Authors ]`). Le champ
  `extraction` des 16 raw porte cette réparation, sans quoi la provenance
  serait fausse : rejouer la commande contre l'EPUB d'origine ne reproduit pas
  les fichiers.
  Options : `--rejoin-lines` (obligatoire, un `<p>` par ligne de PDF),
  `--min-chars 2000`, `--exclude '^Preface$'`. Ni `--strip-page-numbers` (les
  libellés reconstruits n'en portent pas), ni `--relabel`, ni `--absorb`.
  16 raw, 323 763 caractères, aucun `[TABLE]` perdu — `pdftohtml` avait déjà
  aplati les tableaux en lignes entremêlées, ce qui est la vraie limite du
  fichier et a été signalé aux agents.
  **Quatre décisions sur les segments courts**, les quatre ouvertures de partie
  (205, 1 623, 1 661, 1 545 caractères) : fusion en avant acceptée, via
  `--min-chars 2000` plutôt qu'un `--absorb`, qui les aurait recollées au
  chapitre **précédent**. `--min-chars 1500` en laissait trois devenir des
  records d'une page et demie. **Préface exclue** : ses 10 309 caractères
  mélangent un sommaire en prose (« Chapter 2 defines... Chapters 3 and 4
  introduce... »), l'encart O'Reilly Safari, « How to Contact Us » et les
  remerciements. Un record là-dessus est une invitation à la fuite entre
  chapitres. **Foreword gardée** comme chapitre (5 471 caractères, signée Steve
  Portigal) : elle porte l'argument du livre, précédents *Just Enough Research*
  et *Continuous Discovery Habits*. `Index` et `About the Authors` : exclusions
  par défaut.
* **Stage 1.** 16 records, pilote de 3 puis une vague de 4 agents Haiku
  (3 + 3 + 3 + 4). `check_records.py` et `check_claims.py` : **verts avant la
  relecture comme après**, exactement le piège documenté par *Just Enough
  Research*. La relecture complète des 16 records contre le raw par 4 agents
  Sonnet a trouvé **22 défauts sur 12 records** : 7 attributions perdues,
  6 modalisateurs effacés, 4 fabrications, 3 fuites entre chapitres,
  3 réécritures vers le vertueux.
  Le défaut dominant a changé : **l'attribution passe devant les
  modalisateurs**, et la cause est structurelle. Ce livre place dans chacun de
  ses 15 chapitres un encadré d'interview « Voice from the Streets » avec un
  praticien nommé, et trois records citaient directement cet encadré comme si
  c'était la voix des auteurs (Dan Brown, Ofer Deshe, Kyle Soucy). Quatre
  autres présentaient une lecture conseillée (« for more information, see
  *Gamestorming* ») comme la source de l'affirmation. Concepts retirés :
  `[[Mental Model]]` du ch. 13 (le chapitre ne le mentionne jamais, c'est le
  ch. 14) et `[[Improvisation]]` du ch. 8 (simple annonce du ch. 10). Une
  citation du ch. 1 remplacée à la main : verbatim mais portant la césure
  « dis-ruptors » héritée du PDF.
* **Stage 2.** Convergence excellente : 38 noms candidats pour 16 chapitres,
  **33 pointaient déjà sur une page existante**, un seul nom coiné hors de la
  liste fournie (`Data Tracking`). 7 entrées dans `BOOK_MERGES` :
  `Data Tracking` -> `Data Analysis` (le ch. 12 parle de capter les
  observations pendant la session, pas d'instrumentation analytics, donc
  surtout **pas** `Tracking Plan`), plus six clés de vocabulaire non citées
  (`Body Language`, `Microexpressions`, `Nonverbal Cues`, `Debrief`,
  `Debriefing`, `Debrief Sessions`) pour que le prochain livre de recherche
  converge. Fold : 33 pages enrichies, 2 créées (`Debrief Session`,
  `Nonverbal Communication`, toutes deux `stub`). `[[Improvisation]]` laissé
  pendant : un seul record, il part dans `wiki/orphans.md` comme le prévoit
  l'ADR 0003, et l'exception « page créée à la main » de *Laws of UX* ne se
  justifiait que pour dix lois qui structuraient tout le livre.
  **Un seul nouveau `developed`, et c'était le but** : `Active Listening`,
  9 records et 2 ouvrages, `stub` depuis *Articulating Design Decisions* qui
  ne pouvait pas à lui seul lui donner un deuxième ouvrage. Definition et
  Practice écrites, structurées en deux volets (écouter une partie prenante /
  écouter un participant). Prose rafraîchie sur 15 pages `developed` de plus,
  celles qui gagnaient 2 records ou moins de ce livre étant laissées telles
  quelles. Le seul désaccord entre sources explicité dans une page :
  `Bias in Research`, où ce livre soutient qu'un chercheur expérimenté peut
  casser volontairement ses propres règles (question orientée pour créer la
  confiance, question fermée pour mettre à l'aise) là où le reste du corpus
  les pose comme des interdits.
* **Stage 3.** Pas de nouveau thème : le sujet est le coeur de
  `Choosing and Running Research` et de `Research Rigour and Ethics`, tous deux
  déjà en place. `Active Listening` entre en rang 1 dans **deux** thèmes, ses
  neuf records se partageant entre l'écoute des parties prenantes (Greever,
  thème `Influence, Stakeholders and UX Maturity`) et la facilitation d'une
  session (Nunnally et Farkas). `developed unplaced: none`.
* **Route.** Deux garde-fous ajoutés aux scripts, tirés de ce livre.
  `fetch_epub.py` avertit quand un chapitre du plan dépasse 60 000 caractères
  **et** quatre fois la médiane : c'est le symptôme observable d'un NCX qui
  liste des parties au lieu de chapitres, et c'est précisément ce que rien ne
  disait ici. `stage3/generate_themes.py` était **non déterministe** :
  `counter.most_common(2)` départage une égalité par ordre d'insertion, lui-même
  issu d'un `glob()` sur `wiki/episodes` donc de l'ordre du système de fichiers,
  si bien qu'un concept à égalité entre deux thèmes atterrissait ailleurs à
  chaque exécution. Deux lancements consécutifs réécrivaient les 22 fichiers de
  thème avec des « Sharp edges » différentes, du bruit pur dans chaque commit
  d'ingestion. Égalité départagée par nom de thème ; l'idempotence est vérifiée.
* **À faire.** `stage3/check_playbooks.py` signale 19 items ; ce livre en
  ajoute deux (`Card Sorting` et `Data Visualization`), le reste est le retard
  accumulé. Régénération stage 4, à la demande.
* Corpus : 1108 records, 440 concepts (171 `developed`), 859 orphelins.

## 2026-09-10 pipeline livre | Solving Product Design Exercises (Artiom Dashinsky)

* **Stage 0.** EPUB natif propre (un XHTML par section, OPF complet), aucune
  option de réparation nécessaire côté texte. Trois décisions sur les segments
  courts : page de titre exclue, `Validating your solution` et `How much time
  should you spend on each step?` absorbés dans `Step 7`, `Chapter 6:
  Interviews` (171 caractères) laissé fusionner vers le premier entretien.
  Quatre libellés NCX tronqués à 50 caractères par le livre lui-même
  (`Step 3: ...need...`, `Chapter 4: ...inter...`, deux entretiens), réparés
  par `--relabel` depuis le titre complet trouvé en tête de chapitre. 30 raw.
* **Stage 1.** 30 records, Haiku, un pilote de 3 puis deux vagues (3 agents
  de 5, puis 4 agents de 3). `check_records.py` a attrapé 4 citations non
  verbatim, dont une empruntée au chapitre voisin ; `check_claims.py` : 0 sur
  30, le livre est en prose et ne porte aucun tableau. Livre très illustré,
  46 images supprimées à l'extraction : contrainte ajoutée au prompt pour
  qu'aucun record n'affirme ce que montre une illustration.
* **Stage 2.** La liste de candidats donnée aux agents a tenu : 21 records sur
  `Design Exercise`, 14 sur `Product Thinking`, quasi rien à fusionner.
  5 candidats redirigés, 3 clés de vocabulaire en alias. `Hiring and
  Recruitment` promu globalement vers `Design Hiring` (un record NN/g, même
  sens), ce qui donne au concept sa deuxième œuvre et le fait passer
  `developed`. `Product Sense` refusé en alias : NN/g le définit par le
  pattern-matching, pas par le sens large de `Product Thinking`. `Problem
  Solving` mappé vers `Ideation` puis retiré de `BOOK_MERGES` après coup, la
  porte ayant rougi : le record 12 (Step 4) l'emploie pour l'exploration de
  solutions quand `2016-07-31_design-thinking` l'emploie pour la définition du
  problème. Attention, retirer la clé dépose l'alias mais n'annule pas la
  réécriture : `apply_merge.py` était déjà passé, le record 12 citait déjà
  `Ideation` et ne garde que ce nom. 4 pages créées (`Design Exercise`, `Design
  Hiring`, `Product Thinking`, `Storyboarding`), 15 enrichies, 5 nouvelles
  `developed` écrites (`Design Hiring`, `Design Presentation`, `Context of
  Use`, `Design Leadership`, `Value Proposition`), 11 pages `developed`
  existantes rafraîchies avec la matière du livre.
* **Stage 3.** Pas de nouveau thème : le livre tombe dans `Career, Portfolio
  and Case Study`, dont le déclencheur est réécrit pour se lire depuis les
  deux sièges, candidat et hiring manager. 5 gloses ajoutées. `Design
  Exercise` reste en rang 2 et s'attache par co-occurrence à `Design Process
  and Collaboration` et `Product Strategy and Framing`, pas au thème carrière ;
  la route y passe par `Design Hiring`, qui le lie.
* **Route.** Trois leçons, deux passées dans les scripts. `check_records.py` et
  `check_claims.py` prennent `--book SLUG` : le runbook faisait construire la
  liste des basenames dans une variable shell, or zsh ne découpe pas une
  variable non quotée, donc la commande publiée mourait sur « File name too
  long ». `fold_records.py --write` refuse désormais d'écrire quand un alias
  de `BOOK_MERGES` qu'il s'apprête à poser sur une page est cité par un record
  hors du livre : c'est exactement ce qui a fait rougir la porte sur `Problem
  Solving`, après le fold. Le refus ne se déclenche que sur un alias *nouveau*,
  pas sur ceux qu'un livre précédent a déjà posés. Troisième leçon, non
  scriptable : lancer les portes après les notifications de fin de vague, pas
  pendant, les agents réparent leurs propres records.
* Corpus : 1067 records, 426 concepts, 860 orphelins.

## 2026-09-10 pipeline livre | Articulating Design Decisions (Tom Greever)

* **Stage 0.** EPUB O'Reilly natif, 2e édition. Piège du livre : le NCX est de
  profondeur 2, donc chaque sous-section est une entrée et le découpage brut
  donnait 66 segments. Corrigé par `--absorb '^(?!chapter \d+\.|preface)'`, qui
  replie les sous-sections dans leur chapitre. Deuxième piège : les têtes de
  chapitre font 1 000 à 1 500 caractères (l'intro avant la première
  sous-section) et `--min-chars 1500` les fusionnait en avant, collant les
  chapitres deux par deux et envoyant les absorbs dans le mauvais chapitre.
  `--min-chars 1` règle les deux. 12 bruts : préface + 11 chapitres.
* **Perte à l'extraction, découverte à la relecture du 2026-09-10.** `pandoc`
  tourne en `gfm-raw_html` : toute table qu'il ne peut pas rendre en pipe table
  est remplacée par un marqueur `[TABLE]` nu, et `-raw_html` supprime le repli
  HTML qui l'aurait portée. Le contenu disparaît. Huit tables perdues ici, les
  seules du corpus entier : les cinq tables de valeurs par rôle du chapitre 2,
  une au chapitre 1, la table d'objections anticipées du chapitre 3, et une
  étude de cas complète du chapitre 8. Conséquence directe : les records
  affirmaient « nine case studies » au chapitre 8, un décompte des tables
  encore lisibles, alors que le livre en a une de plus. Corrigé. `fetch_epub.py`
  aplatit désormais les cellules avant pandoc, ce qui rend les tables
  représentables en pipe table, et avertit s'il reste un `[TABLE]`
  (`docs/adr/0006`). Les huit tables de ce livre ne sont pas récupérées pour
  autant : `raw/` est append-only, les rendre suppose de réingérer le livre
  depuis l'EPUB, décision ouverte. Les valeurs par rôle du chapitre 2 restent
  sourçables, elles sont reprises en prose plus bas dans la section
  « Stakeholder Stories ».
* **Stage 1.** 12 records, pilote de 3 puis une vague de 3 agents Haiku.
  `check_records` 12 clean. `check_claims` a levé un hit, une vraie
  fabrication : « réduit le délai de livraison de 50 % » attribuée à la
  checklist du chapitre 11, que le chapitre ne dit nulle part (il dit
  « projects would move faster »). Corrigé contre le brut.
* **Stage 2.** Convergence forte sur la liste de candidats : 4 noms hors liste
  sur 12 chapitres. `Trust Building` était déjà un alias de `User Trust`, qui
  désigne la confiance de l'utilisateur dans une interface et non celle du
  stakeholder dans le designer : surchargé via `BOOK_MERGES`. Deux autres
  (`Post-Meeting Follow-Up`, `Stakeholder Feedback Management`) ont été repliés
  à la main dans le record, parce que leur cible était déjà citée dans le même
  record et qu'`apply_merge.py` dédoublonne le frontmatter mais pas les bullets
  `## Concepts`. 4 pages créées, toutes `stub` faute d'un second ouvrage
  (`Design Rationale`, `Design Presentation`, `Active Listening`,
  `Design Leadership`), 10 pages enrichies et réécrites, 1 passage en
  `developed` : `Design Critique` (10 records, 5 ouvrages).
* **Stage 3.** Pas de nouveau thème : `Design Process and Collaboration` et
  `Influence, Stakeholders and UX Maturity` couvrent le sujet, et
  `Design Critique` entre en rank 1 dans les deux. Gloss de
  `Stakeholder Engagement` réécrite, la page étant passée de 13 à 19
  sous-sections. Playbooks frais, aucun thème de playbook touché.
* Corpus : 1037 records, 422 concepts, 861 orphelins sans page.

## 2026-09-08 pipeline livre | The 10x Method (Hexa)

* **Stage 0.** Pas d'EPUB : les sept chapitres sont publics sur
  `media.hexa.com`, extraits à la main le 2026-09-02 puis découpés par
  chapitre le 2026-09-08 depuis un fichier monolithique du second brain.
  `fetch_epub.py` n'a pas tourné. Intégrité vérifiée, 38 500 mots avant et
  après, delta zéro. Résidu accepté : échappements Substack (`1\.`) et
  quelques images sérialisées en blob JSON.
* **Stage 1.** 7 records de chapitre, pilote de 3 puis une vague de 2 agents
  Haiku. `check_records` 7 clean du premier coup. `check_claims` a levé un
  seul hit (`90%`) : le bullet fusionnait trois passages distincts du raw
  (90-100% de DIY, un freelance sous 5 000 €, et le seuil Series A qui parle
  des agences de PR, pas de brand). Corrigé à la main.
* **Stage 2.** Convergence quasi totale sur la liste de candidats fournie aux
  agents : un seul nom hors liste sur 7 chapitres (`Resilience`, fusionné dans
  `Founder Mindset`). 4 pages créées, toutes `stub` faute d'un second ouvrage
  (`Founder Mindset`, `Operating Rituals`, `Design Partner`, `Early Hiring`),
  8 pages enrichies, 1 passage en `developed` : `Team Compensation`
  (6 records, 2 ouvrages, Szigeti et Hexa). Les 7 pages `developed` enrichies
  ont vu leur prose réécrite pour intégrer le livre, au lieu de le citer en
  `## Sources` sans en parler.
* **Stage 3.** Pas de nouveau thème : `Venture Building and Studios` couvre le
  sujet, sa nuance dit maintenant que le troisième livre regarde la
  construction d'entreprise depuis le siège du fondateur et non du studio.
  `Team Compensation` entre en rank 1. 6 gloses corrigées : la réécriture
  stage 2 les avait rendues fausses (`Innovation` annonçait deux échelles, la
  page en a trois).
* Corpus : 1025 records, 418 concepts, 862 orphelins sans page.

## 2026-09-03 pipeline livre | deux ouvrages sur les studios

* **Stage 0.** `fetch_epub.py` : un EPUB devient N raw, un par chapitre,
  découpés sur le NCX (`docs/adr/0005`). *Startup Studio Playbook* (Szigeti,
  2019) : 21 chapitres, EPUB natif. *Venture Studios Demystified* (Kannan et
  Peterman, 2022) : 25 chapitres, EPUB né d'un PDF, lignes et césures
  recollées par `--rejoin-lines`, tableaux laissés en lignes détachées.
* **Stage 1.** 46 records via `prompts/stage1-record-book.md`, pilote de 3
  puis 2 vagues (5 + 4 agents Haiku). Gate à zéro. Deux corrections de prompt
  en route : pas de nom avec slash, `author` = l'ouvrage.
* **Stage 2.** Fold incrémental (`stage2/fold_records.py`) : 23 stubs créés,
  6 pages enrichies, `BOOK_MERGES` appliqué aux seuls records livre. 16
  concepts rédigés en `developed` (11 studio, 5 produit enrichis par les
  livres). Règle des deux ouvrages : `Studio Culture`, 5 records d'un seul
  livre, reste `stub`.
* **Stage 3.** 22e thème, `Venture Building and Studios`, 16 concepts de
  rang 1 dont 5 en double rattachement, 30 sharp edges. Hors playbooks.
* Corpus : 1000 records, 407 concepts (163 `developed`), 860 orphelins.

## 2026-09-03 pipeline livre | Continuous Discovery Habits

* **Stage 0.** *Continuous Discovery Habits* (Teresa Torres, 2021), EPUB natif :
  18 raw (deux avant-propos, introduction, 15 chapitres). Pages de partie et
  intercalaires absorbés dans le chapitre suivant, quatrième de couverture
  exclue. Date de publication prise dans l'OPF (2021-05-18), cohérente avec
  l'édition papier.
* **Stage 1.** 18 records via `prompts/stage1-record-book.md`, pilote de 3
  puis une vague de 3 agents Haiku. Gate à zéro du premier coup, `author`
  correct partout. La liste de 14 candidats fournie au prompt a fait
  converger les agents : 14 noms hors liste seulement, tous fondus par
  `BOOK_MERGES` (12 gardés, 2 retirés pour double sens : `Agency`,
  `Visual Communication`).
* **Stage 2.** Fold incrémental : 7 stubs créés (`Opportunity Solution Tree`,
  `Product Trio`, `Product Outcome`, `Assumption Testing`, `Continuous
  Interviewing`, `Assumption Mapping`, `Experience Map`), 10 pages enrichies,
  5 pages `developed` réécrites avec la matière du livre (`Product Discovery`,
  `User Interviews`, `Decision Making`, `Prioritization`, `Stakeholder
  Engagement`). Aucun nouveau `developed` : règle des deux ouvrages, les 7
  stubs attendent un second livre (Cagan, Patton).
* **Stage 3.** Pas de nouveau thème. Le vocabulaire du livre entre en sharp
  edges sous `Product Strategy and Framing`, `Choosing and Running Research`
  et `Influence, Stakeholders and UX Maturity` ; trigger du routeur et 5
  gloses mis à jour. Playbooks frais.
* **Route.** Deux bugs corrigés dans les scripts : `fold_records.py` réenregistrait
  les alias d'un livre à chaque record (10 doublons sur `Product Discovery`),
  et il avertit désormais quand un alias de `BOOK_MERGES` capture un record
  plus ancien (double sens à trancher avant `--write`). Chemin périmé corrigé
  dans `prompts/stage2-write.md`.
* Corpus : 1018 records, 414 concepts (163 `developed`), 860 orphelins.

## 2026-09-10 pipeline livre | Just Enough Research (Erika Hall)

* **Stage 0.** EPUB natif A Book Apart (2013, 1re édition), NCX propre à
  17 entrées, un fichier HTML par section : aucune option de réparation
  nécessaire (ni `--rejoin-lines`, ni `--strip-page-numbers`, ni `--relabel`).
  11 raw, 247 192 caractères, aucun `[TABLE]` perdu. Deux décisions prises
  seul : `Resources` exclu (annuaire d'outils de 2013, Silverback, Morae,
  Snapz Pro, plus une liste de lectures : c'est de l'appareil éditorial que la
  liste d'exclusion par défaut couvre déjà sous le nom « further readings »),
  et `About A Book Apart` exclu, qui à 361 caractères se faisait sinon
  absorber dans `Resources` par le seuil `--min-chars`. La `Foreword`
  (1933 caractères) est le seul segment court restant : gardée comme chapitre,
  parce qu'elle porte l'argument du livre et qu'elle ouvre le document, donc
  aucun chapitre précédent ne peut l'absorber. Précédent : le foreword de
  *Continuous Discovery Habits* est lui aussi un record.
* **Stage 1.** 11 records, pilote de 3 puis une vague de 3 agents Haiku
  (3 + 2 + 3). `check_records.py` : 11 clean. `check_claims.py` : **0 hit**,
  et c'est précisément ce qui trompe. Les quatre dérives trouvées à la main
  sont toutes hors de portée d'un script qui cherche des chiffres :
  « six questions » là où l'audit concurrentiel en pose sept (nombre écrit en
  lettres, jamais compté), mint.com affirmé là où le livre écrit
  « it's arguable », les cinq composantes de l'utilisabilité présentées comme
  celles du chapitre alors qu'il les attribue à Nielsen, et la conclusion qui
  avait **inversé** « there is no faster way to fail than by testing an idea
  that's still on the drawing board ». Une citation du chapitre 4 remplacée :
  verbatim mais commençant par « It defined stakeholders as », sans son
  antécédent (le mémo du Stanford Research Institute de 1963), donc
  inattribuable pour qui lit le record seul.
* **Stage 2.** Convergence quasi parfaite des candidats : 25 noms pour
  11 chapitres, dont 17 pointaient déjà sur une page existante. Le livre
  plaide pour la recherche plus qu'il ne nomme des méthodes, et le corpus
  couvrait déjà les méthodes. 7 entrées dans `BOOK_MERGES`.
  « Organizational Structure » n'en a **pas** : le nom est déjà un alias
  d'`Organizational Culture` dans le corpus **et** une clé `BOOK_MERGES`
  pointant vers `Studio Structure` depuis les livres studio. Un dict n'a
  qu'une valeur par clé ; le record du chapitre 4 a donc été édité à la main
  pour citer `Organizational Culture` directement, sans toucher à l'alias des
  livres studio. 23 pages enrichies, 2 créées (`Task Analysis`,
  `Competitive Analysis`, toutes deux `stub`), 0 nom pendant. Aucun nouveau
  `developed` : un livre est un ouvrage.
* **Stage 3.** Pas de nouveau thème, le sujet est le cœur de
  `Choosing and Running Research` et de `Research Rigour and Ethics`. Aucun
  `developed` à placer, donc aucune ligne de `theme_prose.py` à écrire. Les
  deux stubs neufs sont atteignables en rang 2, dérivés des records partagés,
  dans deux thèmes chacun. `developed unplaced: none`.
* **À faire.** `stage3/check_playbooks.py` signale 18 items, dont un seul dû à
  ce livre : `Heuristic Evaluation` dans `Usability Heuristics and Evaluation`.
  Le reste est le retard accumulé par les livres précédents. Régénération
  stage 4, à la demande.
* Corpus : 1092 records, 438 concepts (170 `developed`), 858 orphelins.

## 2026-09-11 pipeline livre | The Path to Senior Product Designer (Artiom Dashinsky)

* **Stage 0.** EPUB natif (Pages Publishing), OPF propre : titre, auteur et
  date `2023-09-05` lus tels quels, aucun `--author` ni `--published` forcé.
  NCX plat, 30 entrées, aucune imbriquée et aucun chapitre hors-norme, donc
  aucun des deux pièges des livres précédents. **25 raw**. Décisions :
  `Footnotes` exclu (liste d'URL nue, aucun texte), les quatre pages de partie
  (34 à 37 caractères) laissées en fusion avant, ce qui alimente le champ
  `part`, `Final thoughts` gardé comme chapitre. Options : `--exclude
  '^Footnotes'` et rien d'autre.
* **Stage 1.** **25 records**, pilote de 3 chapitres puis deux vagues de 5 et
  2 agents Haiku. `check_records.py` et `check_claims.py` verts sans reprise
  automatique, **0 hit** `check_claims`.
* **Relecture manuelle.** Dix défauts corrigés à la main, tous invisibles des
  deux gates : un 25% de Mike Davidson chez Twitter transformé en règle
  générale du livre, une analyse personnelle de 120 entreprises de la baie de
  San Francisco présentée comme « des études », une statistique Gallup privée
  de sa source et rétrécie aux product designers, trois décomptes de listes
  faux (« eleven parameters », « six generative techniques », « six
  exercises »), et des attributions perdues (Dropbox, Figma, Linus Pauling,
  Design Career Index). Le livre ne contient aucune épigraphe : le défaut n°1
  du livre précédent était sans objet ici.
* **Stage 2.** La liste de concepts candidats fournie à l'étape 1 a tenu : le
  décompte final ne montre **aucun doublon à fusionner**, `apply_merge.py
  --only` touche 0 record, et `BOOK_MERGES` ne reçoit que du vocabulaire pour
  faire converger le prochain livre. **14 pages enrichies**, **7 créées**
  (`Career Growth Plan`, `Career Ladder`, `Design Competencies`, `Design
  Ownership`, `Mentorship`, `Promotion`, `Design Advocacy`). Six de ces sept
  restent `stub` : une seule œuvre (ADR 0005). `Design Advocacy` fait
  exception, `2017-12-10_bad-design-suggestions` lui donne une seconde œuvre
  et le sort du statut d'orphelin. **4 concepts passent `developed`** et sont
  rédigés : `Design Advocacy`, `Design Strategy`, `Performance Review`,
  `Productivity`. Les 10 pages `developed` qui gagnaient une source sans que
  leur prose la mentionne ont été rafraîchies.
* **Stage 3.** Pas de nouveau thème : le sujet est la carrière, `Career,
  Portfolio and Case Study` existait. `Performance Review` et `Design
  Advocacy` y entrent, `Design Advocacy` aussi dans `Influence, Stakeholders
  and UX Maturity` (la moitié « défendre l'utilisateur »), `Design Strategy`
  dans `Product Strategy and Framing`, `Productivity` dans `Design Process and
  Collaboration`. `developed unplaced: none`. Aucun `PLAYBOOK_THEMES` touché,
  pas de stage 4 à refaire.
* **À noter.** `Career Progression` reste orphelin : son record
  `2024-08-16_stages-of-ux-career-progression` est déjà `processed`, donc
  l'enregistrer comme alias de `Career Ladder` ferait refuser le fold.
* Corpus : 1133 records, 447 concepts (175 `developed`), 855 orphelins.

## 2026-09-10 pipeline livre | Laws of UX (Jon Yablonski, 2e éd.)

* **Stage 0.** EPUB O'Reilly natif, NCX imbriqué à 90 entrées pour 12
  chapitres : chaque `Overview` / `Origins` / `Examples` / `Conclusion` y est
  listé comme une entrée. `--min-chars 1` pour qu'aucune ouverture de chapitre
  ne soit avalée, plus un `--absorb` en lookahead négatif qui replie tout ce
  qui n'est ni `Preface`, ni `A Brief History of Psychology and Design`, ni
  `^\d+\. `. La préface est coupée en deux records : l'avant-propos d'un côté,
  l'histoire de la discipline (Gestalt, facteurs humains, HCI, UX) de l'autre,
  qui porte de la vraie matière. `O'Reilly Online Learning` et
  `How to Contact Us` exclus. 14 raw, 235 691 caractères, aucun `[TABLE]`
  perdu.
* **Stage 1.** 14 records, pilote de 3 puis une vague de 3 agents Haiku
  (4 + 4 + 3). `check_records.py` : 14 clean du premier coup après réparation
  par les agents. `check_claims.py` : 0 hit restant ; les chiffres denses
  (poids de page 2286 Ko en 2023 contre 634 Ko en 2010-2011, seuil 400 ms,
  26 distributeurs et 252 participants chez Kurosu et Kashimura) relus à la
  main contre le raw. `author` correct partout après normalisation du
  guillemetage YAML.
* **Stage 2.** 26 entrées dans `BOOK_MERGES` : chaque loi absorbe les
  paraphrases inventées par son propre chapitre, et une règle explicite pour
  les encadrés du livre (un `PSYCHOLOGY CONCEPT` sans page propre va vers
  `Cognitive Psychology`, sauf s'il est nommé comme un biais, alors
  `Cognitive Bias`). `Chunking` n'est **pas** `Task Chunking`, qui désigne ici
  le découpage d'une to-do list. `Fitts Law` (sans possessif, cité par
  `2016-05-08_expandable-menus`) volontairement pas enregistré comme alias :
  `fold_records.py` refuse l'écriture, ce record déjà `processed` ne pouvant
  pas gagner le backlink que `verify_wiki.py` exigerait ensuite.
  Fold : 36 pages enrichies, 5 stubs créés automatiquement (`Fitts's Law`,
  `Hick's Law`, `Jakob's Law`, `Peak-End Rule`, `Human Factors Engineering`).
  **5 pages créées à la main** (`Miller's Law`, `Postel's Law`,
  `Von Restorff Effect`, `Tesler's Law`, `Doherty Threshold`) : un seul record
  chacune, donc pas de création automatique, mais chacune est le sujet titre
  d'un chapitre entier et laisser `[[Tesler's Law]]` pendre viderait
  l'ingestion de son intérêt. Elles restent `stub`, la règle des deux
  ouvrages n'est pas contournée. `Definition` et `Practice` écrites sur les
  10 pages neuves, et 7 pages `developed` rafraîchies avec la matière du livre
  (`Cognitive Psychology`, `Cognitive Load`, `Cognitive Bias`,
  `Aesthetic-Usability Effect`, `Design Principles`, `Design Consistency`,
  `Deceptive Patterns`). Aucun nouveau `developed` : un livre est un ouvrage.
* **Stage 3.** Pas de nouveau thème, le sujet est déjà couvert. Les 10 lois
  entrent en **rang 1** dans `Psychology, Cognitive Load and Behaviour`, qui
  passe de 10 à 20 concepts, bien qu'elles soient `stub` : laissées en rang 2
  elles étaient tronquées par `MAX_RANK2` et n'étaient plus atteignables que
  depuis `wiki/index.md`. Aucune dans un `PLAYBOOK_THEMES`. Ligne de
  déclenchement du routeur réécrite pour nommer les lois.
* **Route.** Un défaut de comptage corrigé dans `generate_themes.py` et
  `fold_records.py` : les bullets `- [[record]]` étaient comptés comme sources
  partout dans la page, pas seulement sous `## Sources`. 16 pages gonflaient
  leur compteur (`Information Architecture` affichait 73 pour 65), et dans
  `fold_records.py` ce comptage décide du passage en `developed`.
* **À faire.** `stage3/check_playbooks.py` signale les 6 playbooks comme
  périmés : ce livre a enrichi des pages qui les alimentent. Deux seulement
  ont vu leur prose changer (`Aesthetic-Usability Effect`, `Design
  Principles`), les autres n'ont gagné qu'une ligne de `## Sources`.
  Régénération stage 4, à la demande.
* Corpus : 1081 records, 436 concepts (163 `developed`), 856 orphelins.

## 2026-09-11 ingestion | *Product Management for UX People* (Crumlish, 2022)

* **Stage 0.** 14 raw depuis l'EPUB Rosenfeld Media : FAQ, foreword,
  introduction, 11 chapitres numerotes. `fetch_epub.py --min-chars 1
  --exclude '^How to Use This Book' --exclude '^Footnotes' --absorb
  '^(?!CHAPTER \d+:|Foreword|Introduction|Frequently Asked Questions)'`.
  L'absorb en lookahead negatif est ce qui tient le decoupage : dans ce NCX,
  chaque sous-section a son entree, et sans lui le plan explosait en dizaines
  de fragments. **Pas de chapitre d'interviews en fin d'ouvrage** malgre
  l'habitude Rosenfeld : les voix de praticiens sont des encadres
  `FROM THE TRENCHES` et `A DAY IN THE LIFE OF A ... PM` a l'interieur des
  chapitres, donc absorbes avec eux, ce qui est le bon sort. Sept chapitres
  portent un « day in the life » nominatif.
* **Stage 1.** Pilote de 3 records repris de la session precedente et
  reecrit : il avait perdu toutes les attributions nominatives et comptait
  quatre archetypes de PM la ou le chapitre 1 en deroule cinq. Le prompt de
  la vague a ete durci la-dessus (encadres nommes, modalisateurs conserves,
  comptage avant d'ecrire un nombre). Deux vagues Haiku, 3 puis 2 agents,
  11 records. `check_records.py` et `check_claims.py` verts, **zero hit
  numerique** sur 14 records, le meilleur ratio des livres ingeres.
  Six defauts trouves a la main **sous des gates vertes**, tous du meme
  genre : une reserve du raw durcie en regle (« contacter un client une fois
  par semaine », les 40 % de product-market fit, la perte de 10 % par etape
  de funnel), une regle inventee (« au moins 2000 utilisateurs par bucket »
  la ou le raw dit seulement de ne pas s'etonner que ca se stabilise vers
  2000), et des praticiens nommes disparus, dont les deux desaccords de
  B. Pagels-Minor avec le chapitre 8 et le mnemonique AARRR non credite a
  Dave McClure.
* **Stage 2.** Fusion quasi vide, comme voulu : 34 noms candidats, 33 deja
  des pages, une seule coinage (`Estimation` -> `Agile Development`). Quatre
  cles de vocabulaire enregistrees pour le prochain livre produit
  (`Product Owner`, `Definition of Done`, `Story Points`,
  `Effort Estimation`). Fold : 33 pages enrichies, **0 creee**, 0 lien
  pendant. Deux passages en `developed` sous la regle des deux ouvrages :
  `Product Management` (9 records, 4 ouvrages) et `Assumption Testing`
  (5 records, 2 ouvrages), ecrits de zero. 21 pages `developed` rafraichies
  par integration, jamais par reecriture. Les desaccords internes au livre
  sont conserves nommes : Matt LeMay contre l'obligation d'aimer les
  chiffres, Clement Kao sur l'A/B testing impraticable en entreprise,
  B. Pagels-Minor contre le break-even comme metrique de succes.
* **Stage 3.** Pas de nouveau theme. `Product Management` en rang 1 dans
  `Product Strategy and Framing` et dans `Career, Portfolio and Case Study`
  (la bascule UX vers produit est une bifurcation de carriere, pas seulement
  une discipline). `Assumption Testing` en rang 1 dans
  `Product Strategy and Framing` et dans
  `Measurement, Metrics and Business Impact`, ou il porte les alternatives a
  l'A/B test. `developed unplaced: none`.
* **A faire.** `check_playbooks.py` reste rouge, mais pour l'essentiel depuis
  les livres precedents : ce livre n'a touche qu'un concept de playbook
  (`Information Architecture`). Regeneration stage 4 a la demande.
* Corpus : 1147 records, 447 concepts (177 `developed`), 858 orphelins.

## 2026-09-11 ingestion | *Storytelling in Design* (Anna Dahlström, 2019)

* **Stage 0.** 15 raw depuis l'EPUB O'Reilly natif (metadonnees OPF :
  titre *Storytelling in Design*, auteure Anna Dahlström, `dc:date`
  2019-12-17, ISBN 9781491959428 qui donne l'URL O'Reilly).
  `fetch_epub.py --min-chars 1 --exclude '^\[ Index \]$'
  --absorb '^(?!chapter \d+\.|\[)'`. **NCX imbrique** : 118 entrees pour
  15 chapitres (une preface + 14 chapitres), chaque sous-section ayant la
  sienne. Ici le lookahead negatif n'a pas eu besoin d'enumerer les titres,
  contrairement a *User Story Mapping* : les ouvreurs de chapitre sont
  tous libelles « Chapter N. » et aucune sous-section ne commence par ce
  mot, donc `^(?!chapter \d+\.|\[)` suffit, le `\[` protegeant
  `[ Preface ]`. `--min-chars 1` reste indispensable : les 14 ouvreurs
  font 81 a 161 caracteres et partaient en avant avec la valeur par
  defaut. `[ Index ]` exclu a la main, les crochets de son libelle
  l'empechant de matcher `^index\b` de `DEFAULT_EXCLUDE`. Aucune autre
  entree O'Reilly dans le NCX : la page de titre, le copyright et le
  « How to Contact Us » sont en amont du premier point de coupe et tombent
  d'eux-memes. Aucun residu d'image malgre les 37 Mo du fichier, aucun
  `[TABLE]`, aucun avertissement de chapitre hors normes (le plus gros,
  chapitre 6, fait 90 227 c. pour une mediane de ~45 000).
* **Stage 1.** Pilote de 3 records (preface, chapitre 1, chapitre 2), puis
  une vague de 4 agents Haiku et une vague de 2. `check_records.py` 0
  probleme, `check_claims.py` 0 hit residuel — mais un hit reel attrape en
  vague A : un record affirmait « 400 hours of content every hour » sur
  YouTube et « 3.7 million broadcasters » sur Twitch, deux chiffres absents
  du raw, connaissance externe pure. `check_claims.py` a signale le 400 et
  **rate le 3,7 million** (decimal), ce qui vaut d'etre su.
* **`check_names.py`, premiere utilisation reelle.** 31 hits apres la
  vague A sur 12 records, 6 apres la vague B sur 3. Vraies attributions
  perdues et restaurees : Walt Disney (preface), Johannes Gutenberg et
  Peter Guber / *Tell to Win* (ch. 1), Gotthold Ephraim Lessing et Joanna
  Ngai (ch. 2), Paul Joseph Gulino et Robert Towne (ch. 5), IDEO sur
  l'empathie (ch. 6), Jerry Jenkins et le contrepoint d'Ali Luke (ch. 13).
  Bruit majoritaire : acronymes pris pour des noms (`CMO`, `CTA`, `SVP`,
  `AIs`), personnages de fiction (Chuck Nolan, CEO Nathan), legendes de
  figures (Chooseco, Silk King), pays (Sweden), notes de bas de page
  (Tisch School, Forbes). Ordre de grandeur : ~1 hit sur 3 etait une vraie
  attribution manquante, le reste du bruit lisible en une ligne.
* **Defaut non couvert par les trois gates** : sept citations tierces
  etaient tombees dans `## Quotes` sans etre creditees (Steve Jobs,
  Hitchcock, Joseph Campbell, Robert McKee, Barri Evins, Daniel Dercksen,
  Joe Berkowitz). `check_records.py` les valide, elles sont verbatim ; rien
  ne dit qu'elles ne sont pas de l'auteure. Corrigees a la main, et la
  regle a ete ajoutee au prompt de la vague B, qui l'a respectee.
* **Stage 2.** 30 candidats apres la vague, 2 fusions : `Transmedia
  Storytelling` -> `Storytelling` (une forme de narration, pas un service
  omnicanal) et `Product Life Cycle` -> `Customer Journey` (le sens de
  Dahlström est le parcours de l'utilisateur, pas le sens PM
  introduction/croissance/maturite/declin ; un futur ouvrage PM devra
  forger `Product Lifecycle Management` plutot que reutiliser la cle).
  7 pages creees, toutes `stub` faute d'un second ouvrage : `Narrative
  Structure` (8 records), `Experience Shape` (5), `Red Thread` (5),
  `Scene Structure` (4), `Character Development` (2), `Nonlinear
  Storytelling` (2), `Subplot` (2). 23 pages enrichies. Vocabulaire
  enregistre en alias (Dramaturgy, Three-Act Structure, Plot Point, Story
  Shape, Through Line, CYOA, Branching Narrative...) pour que le prochain
  livre de narration converge.
* **Trois concepts passent `developed`** grace au deuxieme ouvrage, ce qui
  etait le but : `Shared Understanding` (10 records, 2 works), `User Flow`
  (5, 5), `Wireframing` (5, 5). Definition et Practice ecrites, dont un
  desaccord garde explicite sur `Wireframing` (NN/g en fait une etape
  normale, Penchenat declare l'ere du wireframe terminee).
* **Stage 3.** Aucun theme neuf : la narration est une methode qui traverse
  les themes existants. `Shared Understanding` et `Wireframing` places dans
  `Design Process and Collaboration`, `User Flow` dans `Journeys, Service
  and Omnichannel`. Glosses ecrites pour les trois. `developed unplaced:
  none`, 193 concepts rang 1, 193 glosses.
* **A faire.** `check_playbooks.py` signale des playbooks perimes, mais ils
  l'etaient deja avant ce livre (dates de distillation 2026-07-31 contre
  des pages mises a jour les 10 et 11 septembre) : dette anterieure, non
  creee ici. Les sept pages de narration attendent un deuxieme ouvrage
  pour passer `developed`.
* Corpus : 1185 records, 461 concepts (183 `developed`), 854 orphelins.

## 2026-09-11 ingestion | *User Story Mapping* (Jeff Patton avec Peter Economy, 2014)

* **Stage 0.** 23 raw depuis l'EPUB O'Reilly natif (un fichier HTML par
  chapitre, OPF propre, `dcterms:modified` 2014-09-05 retenu comme date de
  publication ; `--author "Jeff Patton, Peter Economy"` parce que l'OPF ne
  declare que Patton). `fetch_epub.py --min-chars 1 --exclude
  '^User Story Mapping$' --exclude '^Colophon$' --exclude '^Safari'
  --exclude '^How to Contact Us$' --absorb '^(?!(Foreword by |Preface$|Read
  This First$|1\. The Big Picture$|...|18\. Learn from Everything You
  Build$))'`. **NCX imbrique** : 213 entrees pour 23 chapitres, chaque
  sous-section ayant la sienne. Le lookahead negatif enumere les 23 titres
  exacts plutot qu'un motif `^\d+\.` : les chapitres 5, 6 et 14 ont des
  sous-sections elles-memes numerotees (« 1. Card », « 2. Conversation »,
  « 1. Frame the Idea »), qu'un motif generique aurait promues en chapitres.
  `--min-chars 1` est indispensable ici : plusieurs ouvreurs de chapitre font
  moins de 1 000 caracteres (« 16. Refine, Define, and Build » : 188), et
  avec la valeur par defaut ils partaient en avant dans le chapitre suivant
  avant d'avoir pu absorber leurs propres sous-sections. Exclusions O'Reilly
  absentes de `DEFAULT_EXCLUDE` : page de titre, Safari Books Online, How to
  Contact Us, Colophon. « The End, or Is It? » absorbe dans le chapitre 18.
  Aucun `[TABLE]`, aucun avertissement de chapitre hors normes.
* **Stage 1.** Pilote de 3 records (une preface invitee, un chapitre a
  histoire d'entreprise, un chapitre dense), puis une vague de 4 agents
  Haiku a 5 chapitres. `check_records.py` 0 probleme. `check_claims.py` :
  un seul hit, « 1980s arcade game » pour *Asteroids*, absent du raw qui dit
  seulement « an early video game » et « the old Atari game » — corrige.
  Trois defauts d'attribution rattrapes a la relecture, tous du meme type :
  Chris Shinkle (SEP) et ses « Risk Stories » au chapitre 4, Alistair
  Cockburn credite de l'*information radiator* au chapitre 8, David Hussman
  pour Cardboard (chapitre 8) et pour la metaphore du producteur
  (chapitre 12). Un modalisateur ecrase remis en place au chapitre 1 : le
  raw decrit l'impossibilite de dater une carte (« a couple hours, days,
  weeks, or maybe a month—who knew? »), le record en avait fait une regle de
  dimensionnement.
* **Stage 2.** 34 noms candidats, 30 apres fusion, sept coinages sans
  variante rivale (`Story Mapping`, `User Story`, `Shared Understanding`,
  `Product Backlog`, `Story Slicing`, `Validated Learning`,
  `Release Planning`). Quatre singletons redirectionnes : `Story Workshop` ->
  `Workshop Facilitation`, `Opportunity` -> `Product Discovery` (et non
  `Opportunity Solution Tree`, qui est l'artefact de Torres),
  `Product Vision` -> `Product Strategy`,
  `Design and Development Collaboration` -> `Team Collaboration`. Deux alias
  volontairement non poses, faute de pouvoir gagner le backlink d'un record
  deja `processed` : `User Stories` (2022-05-15_two-tips-better-ux-storytelling,
  ou le mot designe une histoire racontee sur les utilisateurs, pas une unite
  de livraison) et `Backlog Management` (2019-10-06_ux-agile-backlog, meme
  sens pourtant — le promouvoir dans `MERGES` aurait entraine `User Stories`
  par le singleton map). 7 pages creees, 23 enrichies. **Trois pages passent
  en `developed` grace au deuxieme ouvrage** : `Story Mapping` (8 records,
  2 works), `Product Outcome` (12, 2), `Product Trio` (9, 2). Les six autres
  creations restent `stub` : un seul work (docs/adr/0005). 19 pages
  `developed` existantes rafraichies par integration. Desaccords conserves
  nommes : le trio de Torres (PM, designer, ingenieur) contre la triade de
  Patton (2 a 4 personnes menees par un product owner) et contre ses « three
  amigos » de story workshop ; la story map jetable et par-idee de Torres
  contre la backbone et le decoupage en releases de Patton ; le product owner
  de Patton contre le « pas un product owner » de Crumlish.
* **Stage 3.** Pas de nouveau theme. `Story Mapping` en rang 1 dans
  `Product Strategy and Framing` et dans `Design Process and Collaboration`
  (c'est une activite de groupe autant qu'un artefact de planification),
  `Product Outcome` dans `Product Strategy and Framing` et
  `Measurement, Metrics and Business Impact`, `Product Trio` dans
  `Design Process and Collaboration`. La trigger line de
  `Product Strategy and Framing` annoncait le product trio et les outcomes en
  sharp edges : reecrite, ils sont rang 1. `developed unplaced: none`.
* **A faire.** Aucun theme de playbook touche, `check_playbooks.py` non
  relance. Le vocabulaire de livraison creee ici (`User Story`,
  `Product Backlog`, `Story Slicing`, `Release Planning`,
  `Shared Understanding`) attend un deuxieme ouvrage agile pour passer
  `developed`.
* Corpus : 1170 records, 454 concepts (180 `developed`), 854 orphelins.

## Ingestions
* 2024-05 -> 2026-06 : 90 épisodes Parlons Design (YouTube + Substack), ingérés avant la migration.
* 2026-09-03 : 2 livres (46 chapitres), `fetch_epub.py`, stages 0 à 3 complets.
* 2026-09-03 : *Continuous Discovery Habits* (18 chapitres), stages 0 à 3 complets.
* 2026-09-08 : *The 10x Method* (7 chapitres), extraction manuelle, stages 0 à 3 complets.
* 2026-09-10 : *Articulating Design Decisions* (12 chapitres), `fetch_epub.py`, stages 0 à 3 complets.
* 2026-09-10 : *Solving Product Design Exercises* (30 chapitres), `fetch_epub.py`, stages 0 à 3 complets.
* 2026-09-10 : *Laws of UX* (14 chapitres), `fetch_epub.py`, stages 0 à 3 complets.
* 2026-09-10 : *Just Enough Research* (11 chapitres), `fetch_epub.py`, stages 0 à 3 complets.
* 2026-09-10 : *UX Research* (16 chapitres), `fetch_epub.py` sur un NCX reconstruit à la main, stages 0 à 3 complets.
* 2026-09-11 : *The Path to Senior Product Designer* (25 chapitres), `fetch_epub.py`, stages 0 à 3 complets.
* 2026-09-11 : *Product Management for UX People* (14 chapitres), `fetch_epub.py`, stages 0 a 3 complets.
* 2026-09-11 : *Storytelling in Design* (15 chapitres), `fetch_epub.py`, stages 0 a 3 complets.
