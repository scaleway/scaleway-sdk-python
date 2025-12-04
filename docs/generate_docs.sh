#!/bin/bash

# Chemins vers les packages racines (doivent contenir __init__.py et des sous-modules)
SCALEWAY_PKG="../scaleway/scaleway"
CORE_PKG="../scaleway-core/scaleway_core"
ASYNC_PKG="../scaleway-async/scaleway_async"

# Vérifier que les dossiers racines existent et sont bien des packages
for pkg in "$SCALEWAY_PKG" "$CORE_PKG" "$ASYNC_PKG"; do
  if [ ! -d "$pkg" ]; then
    echo "❌ Erreur : Le dossier '$pkg' n'existe pas."
    exit 1
  fi
  if [ ! -f "$pkg/__init__.py" ] ; then
    echo "⚠️  Attention : '$pkg' ne semble pas être un package Python (pas de __init__.py)."
  fi
  echo "✅ Package trouvé : $pkg"
done

# Exporter PYTHONPATH pour que tous les modules soient accessibles
export PYTHONPATH="..:$PYTHONPATH"

# Générer la doc pour chaque package racine (pdoc explore automatiquement les sous-modules)
echo "📚 Génération de la documentation avec pdoc..."
poetry run pdoc \
  -o html \
  -d google \
  "$SCALEWAY_PKG" \
  "$CORE_PKG" \
  "$ASYNC_PKG"

if [ $? -eq 0 ]; then
  echo "✅ Documentation générée avec succès dans le dossier 'html/'."
else
  echo "❌ Échec de la génération de la documentation."
  exit 1
fi