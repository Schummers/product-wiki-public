#!/usr/bin/env bash
# Publie un snapshot du repo prive vers Schummers/product-wiki-public :
# un seul commit, sans historique, sans le texte brut des livres (type: book).
# Le prive reste la seule source ; le public est ecrase a chaque appel.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
PUBLIC_REMOTE="${PUBLIC_REMOTE:-https://github.com/Schummers/product-wiki-public.git}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

cd "$ROOT"
[[ -z "$(git status --porcelain)" ]] || { echo "arbre non commite, abandon" >&2; exit 1; }
git archive HEAD | tar -x -C "$WORK"

cd "$WORK"
grep -l '^type: book' raw/sources/*.md | xargs rm -f
[[ "$(grep -l '^type: book' raw/sources/*.md 2>/dev/null | wc -l)" -eq 0 ]]
if grep -rlF "$HOME" . --include='*.md' --include='*.py' --include='*.sh' >/dev/null; then
  echo "chemin absolu personnel dans le snapshot, abandon" >&2; exit 1
fi
# Noms propres. Le script et sa liste vivent dans ai-os, source unique pour les
# deux depots publics. Ajoute le 2026-09-13, apres avoir trouve 21 mentions du
# proprietaire dans un snapshot publie depuis des mois.
# raw/sources/ est exempte : c'est du materiel externe recopie verbatim, ou un
# nom de tiers (auteur cite, intervenant de podcast) n'est pas une fuite. Le
# contrat du repo dit que rien de ce dossier n'appartient au proprietaire.
AIOS_ROOT="${AIOS_ROOT:-$ROOT/../..}"
CHECK_NAMES="$AIOS_ROOT/system/scripts/check-public-names.py"
[[ -f "$CHECK_NAMES" ]] || { echo "check-public-names.py introuvable ($CHECK_NAMES), abandon" >&2; exit 1; }
python3 "$CHECK_NAMES" . --exempt raw/sources || { echo "check-public-names a echoue, abandon" >&2; exit 1; }

git init -q -b main
git add -A
git -c user.name="$(cd "$ROOT" && git config user.name)" \
    -c user.email="$(cd "$ROOT" && git config user.email)" \
    commit -q -m "chore: public snapshot $(date +%F) from $(cd "$ROOT" && git rev-parse --short HEAD)"
git remote add origin "$PUBLIC_REMOTE"
git push --force origin main
echo "publie : $(git rev-parse --short HEAD), $(git ls-files | wc -l | tr -d ' ') fichiers, sources : $(ls raw/sources | wc -l | tr -d ' ')"
