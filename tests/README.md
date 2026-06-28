# Dossier de tests — RAG Correctif Offline

Ce dossier contient la documentation des tests permettant de vérifier le bon fonctionnement du pipeline RAG correctif.

## Contenu du dossier

- **test_ingestion.md**  
  Vérifie la lecture des fichiers Markdown, la génération des chunks, la création des embeddings BGE et le stockage persistant dans ChromaDB.

- **test_retrieval.md**  
  Valide la recherche vectorielle : cohérence des passages retournés, pertinence sémantique et intégrité de la base vectorielle.

- **test_rag_complet.md**  
  Teste le pipeline complet : reformulation, retrieval, vérification de pertinence, correction éventuelle et réponse finale augmentée.

## Test automatique global

Le script `run_tests.py` exécute automatiquement les trois étapes de validation :

1. ingestion & embeddings  
2. recherche vectorielle  
3. pipeline RAG complet

Il permet de vérifier rapidement que le système fonctionne sans erreur.

## Objectif

Ce dossier fournit une preuve de validation claire, simple et reproductible, adaptée aux besoins des PME/TPE souhaitant un assistant IA fiable, local et sans cloud.
