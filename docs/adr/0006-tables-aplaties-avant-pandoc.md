# 0006 — Les tableaux sont aplatis avant pandoc, pas abandonnés à `[TABLE]`

Date : 2026-09-10
Statut : accepté, implémenté (`fetch_epub.py`, `flatten_table_cells()`)

## Contexte

Le stage 0 convertit le HTML de l'EPUB avec `pandoc -f html -t gfm-raw_html
--wrap=none` (`fetch_epub.py`). Le `-raw_html` est délibéré et ancien : il jette
les `<span>` de Calibre et garde `raw/` en Markdown propre, lisible, greppable,
au lieu d'une soupe HTML.

Ce que personne n'avait vu, c'est ce qu'il coûte. Le writer gfm de pandoc ne
sait exprimer qu'un tableau dont les cellules contiennent de l'inline. Une
cellule qui porte une liste, plusieurs paragraphes ou un titre n'est pas
représentable en pipe table. Avec `raw_html` actif, pandoc se rabat sur le
`<table>` HTML brut. Avec `-raw_html`, il n'a plus de repli : il écrit un
marqueur `[TABLE]` nu et **le contenu disparaît**. Aucun avertissement, aucun
code de sortie, rien dans le dry-run.

Vérifié sur pandoc 3.11 :

```
$ pandoc -f html -t gfm-raw_html --wrap=none   # cellule contenant une <ul>
[TABLE]
$ pandoc -f html -t gfm --wrap=none            # le même document
<table> ... </table>                           # contenu préservé, en HTML
```

Découvert le 2026-09-10 en relisant l'ingestion de *Articulating Design
Decisions* contre ses bruts. Huit tableaux perdus, les seuls `[TABLE]` du corpus
entier : les cinq tableaux de valeurs par rôle sur lesquels tout le chapitre 2
est construit, un au chapitre 1, la table des objections anticipées du chapitre
3, et une étude de cas complète du chapitre 8.

La perte ne s'arrête pas au brut. Un record écrit contre un fichier mutilé
comble le trou sans le savoir : celui du chapitre 8 annonçait « nine case
studies », un décompte des tableaux encore lisibles, alors que le livre en porte
un de plus. Le brut est la référence d'audit du corpus, `check_records.py` et
`check_claims.py` vérifient les records contre lui. Un brut amputé rend les
gates verts sur un texte qui n'existe plus.

Les six autres livres de la bibliothèque en attente contiennent des tableaux.
Décider maintenant coûte moins que réingérer plus tard : `raw/` est append-only,
donc revenir sur un livre déjà ingéré veut dire supprimer et refaire ses raw,
ses records, et repasser les stages 2 et 3.

## Décision

**Les cellules de tableau sont aplaties en inline avant d'atteindre pandoc.**
`flatten_table_cells()` tourne dans `prepare_html()`, qui manipule déjà la
soupe : chaque `<ul>`, `<ol>`, `<p>`, `<div>`, `<blockquote>` ou titre à
l'intérieur d'un `<td>`/`<th>` est remplacé par son texte, les éléments de liste
joints par « ; ». Le tableau redevient représentable, pandoc l'écrit en pipe
table, `-raw_html` reste actif.

**On perd la mise en forme, on garde les mots.** C'est le bon côté de l'échange :
un record cite ce que dit une source, jamais comment elle le dispose. Rien dans
`SCHEMA.md` ne demande à un record de restituer une structure de tableau.

**Le garde-fou `[TABLE]` reste en place**, en filet. L'aplatissement traite les
cas connus, pas tous les cas possibles (tableau imbriqué dans un tableau,
construction que pandoc refuse pour une autre raison). Si un `[TABLE]` sort
malgré tout, le dry-run le nomme, chapitre par chapitre, et dit de ne pas
affirmer ce qu'il contenait ni de compter les éléments d'une liste amputée.

**Les huit tableaux déjà perdus ne sont pas récupérés.** Les affirmations qu'ils
avaient induites sont corrigées dans les records et les pages concepts, et la
perte est consignée dans `wiki/log.md`. Rendre le contenu suppose de réingérer
le livre depuis l'EPUB, ce qui reste ouvert et se décide séparément.

## Alternatives écartées

**Réactiver `raw_html` (`-t gfm`).** Écartée. Elle préserve le contenu, testé et
vérifié, mais fait entrer du HTML dans `raw/` : non seulement les tableaux, mais
tout ce que pandoc ne sait pas exprimer, à commencer par les `<span>` de Calibre
que `-raw_html` avait justement pour but de jeter. Elle change la forme de tous
les bruts futurs et rend le corpus hétérogène, l'ancien en Markdown, le nouveau
en Markdown plus HTML. On paierait la réparation d'un cas par la dégradation de
tous les autres.

**Accepter la perte et se contenter d'avertir.** C'était l'état des choses entre
la découverte et cet ADR, et c'est insuffisant : un avertissement déplace la
charge sur le lecteur de chaque ingestion, alors que le contenu est récupérable
mécaniquement. Un garde-fou qui signale ce qu'on savait réparer est une dette,
pas une décision.

**Convertir les tableaux en listes de définitions ou en prose.** Écartée : elle
demande d'interpréter le rôle des colonnes, donc du jugement, donc un modèle,
au stage 0 qui n'en a aucun et n'en veut pas (`SCHEMA.md`, tableau des stages :
« 0 Scrape, none, pure script »).

**Extraire les tableaux à part, dans un fichier annexe.** Écartée : elle casse
la règle un raw = un chapitre et laisserait les tableaux hors du texte que
`check_claims.py` lit.

## Conséquences

- La forme des bruts change pour les livres à venir : un pipe table apparaît là
  où un `[TABLE]` serait sorti. C'est une amélioration stricte, pas une rupture,
  et les bruts déjà écrits ne sont pas touchés.
- L'aplatissement s'applique à **tous** les tableaux, y compris ceux qui
  passaient déjà. Sans effet sur eux : une cellule sans contenu bloc n'est pas
  modifiée, vérifié.
- `--rejoin-lines` tourne après l'aplatissement, donc un EPUB né d'un PDF voit
  ses cellules aplaties avant le recollage des lignes. Le résidu noté dans
  l'ADR 0005 (« les tableaux et figures d'un EPUB né d'un PDF sortent en lignes
  détachées ») reste vrai pour les figures, et se réduit pour les tableaux.
- Le champ `extraction` des bruts ne mentionne pas l'aplatissement : il consigne
  la ligne de commande, et celle-ci ne change pas. La version du comportement se
  lit dans l'historique git de `fetch_epub.py`. Accepté, à revoir si un jour
  deux comportements d'extraction doivent coexister.
- À rouvrir si un livre arrive avec des tableaux dont la structure porte le sens
  et pas seulement les mots, une matrice de décision par exemple. Le choix serait
  alors local à ce livre, pas global au pipeline.
