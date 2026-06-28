# Test Ingestion & Embeddings

## Objectif
Vérifier que :
- les fichiers Markdown sont correctement lus,
- les chunks sont générés sans erreur,
- les embeddings BGE sont créés,
- ChromaDB stocke les vecteurs en mode persistant.

## Procédure
1. Exécuter :
   python ingest.py

2. Vérifier :
- création du dossier `chroma_db/`
- absence d’erreurs dans la console
- nombre de documents ingérés cohérent

## Résultat attendu
- Embeddings générés
- Base vectorielle persistante créée
- Aucun message d’erreur
