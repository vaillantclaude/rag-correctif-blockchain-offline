![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Offline](https://img.shields.io/badge/Mode-100%25_Offline-success)
![RAG](https://img.shields.io/badge/Architecture-RAG_Correctif-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![Gemma](https://img.shields.io/badge/LLM-Gemma_4_12B-red)

Ce projet démontre la création d’un assistant IA 100% offline basé sur un pipeline RAG correctif. 
Il utilise Gemma 4, BGE et ChromaDB pour fournir des réponses fiables à partir d’un corpus Markdown local. 
L’architecture est simple, sécurisée, reproductible et adaptée aux PME/TPE souhaitant intégrer l’IA sans cloud. 
Ce repository présente l’architecture, les scripts, le pipeline et les choix techniques. 
C’est un projet professionnel démontrant la maîtrise des LLM locaux et de la gouvernance IA.

# Projet : RAG Correctif Local basé sur Markdown
## Gemma 4 + BGE + ChromaDB — 100% Offline

## 1. Objectifs du projet
Ce projet met en place un RAG correctif 100% local, conçu pour fonctionner hors ligne, sans aucune dépendance cloud, et basé exclusivement sur des fichiers Markdown.

L’objectif est de créer un assistant IA fiable, spécialisé blockchain, capable de :
- reformuler les questions,
- vérifier la pertinence des résultats,
- corriger les recherches,
- répondre uniquement à partir des documents Markdown.

Objectifs principaux :
- Construire un assistant IA local basé sur mes cours Markdown.
- Garantir un fonctionnement offline complet (aucune API, aucun cloud).
- Utiliser un pipeline RAG correctif, plus fiable qu’un RAG simple.
- S’appuyer sur des outils gratuits, simples, open source.
- Assurer une architecture stable, maintenable, reproductible.

## Pourquoi ce projet est utile en entreprise

Ce projet répond à des besoins réels des PME/TPE qui souhaitent intégrer l’IA de manière sécurisée, simple et efficace.

### ✔️ 1. 100% Offline — aucune fuite de données
Le système fonctionne entièrement en local :
- aucun cloud,
- aucun envoi de données,
- aucune dépendance externe.

Idéal pour les entreprises sensibles (finance, santé, industrie, collectivités).

### ✔️ 2. Basé sur les documents internes
Le RAG utilise uniquement :
- les fichiers Markdown internes,
- les procédures,
- les formations,
- les documents métier.

L’IA devient un **assistant interne** spécialisé dans le métier de l’entreprise.

### ✔️ 3. Pipeline correctif = fiabilité accrue
Contrairement à un RAG simple :
- la question est reformulée,
- la pertinence est vérifiée,
- la recherche est corrigée si nécessaire.

Résultat :
- moins d’hallucinations,
- réponses plus précises,
- meilleure cohérence.

### ✔️ 4. Coût nul — matériel existant
Le système tourne sur :
- un Mac,
- un PC,
- un serveur interne.

Sans abonnement, sans API, sans cloud.

### ✔️ 5. Architecture simple et maintenable
Les composants sont :
- LM Studio,
- ChromaDB,
- BGE,
- Python.

Tous gratuits, open source, faciles à maintenir.

### ✔️ 6. Reproductible dans n’importe quelle PME
L’entreprise peut :
- ajouter ses propres documents,
- adapter le corpus,
- créer son assistant métier,
- étendre le système à d’autres services.

C’est une base solide pour un **assistant IA interne**.

## 2. Architecture technique retenue
L’architecture repose sur 5 composants locaux, simples, gratuits et robustes.

### 2.1 Modèle IA local (LLM)
Modèle utilisé : Gemma 4 12B QAT (via LM Studio)

Raisons du choix :
- excellente compréhension des questions techniques,
- très bon en reformulation, vérification, raisonnement,
- idéal pour un RAG correctif,
- fonctionne 100% en local,
- rapide et stable sur Mac.

Gemma est utilisé pour :
- reformuler la question,
- vérifier la pertinence des passages trouvés,
- corriger la recherche si nécessaire,
- générer la réponse finale.

Gemma peut être exécuté localement dans LM Studio avec support GGUF, entièrement sur la machine de l’utilisateur. [web:12][web:14]

### 2.2 Embeddings locaux
Modèle utilisé : BGE Small v1.5 (GGUF)

Chemin exact :

```text
~/.lmstudio/models/CompendiumLabs/bge-small-en-v1.5-gguf/bge-small-en-v1.5-q8_0.gguf
```

Raisons du choix :
- gratuit,
- simple à installer via LM Studio,
- excellent sur du texte technique,
- parfaitement adapté aux fichiers Markdown,
- fonctionne hors ligne,
- très performant pour la recherche sémantique.

### 2.3 Base vectorielle locale
Base utilisée : ChromaDB (mode persistant)

Raisons :
- installation simple,
- stockage local,
- API claire et lisible,
- parfait pour un pipeline correctif,
- aucune dépendance externe,
- supporte très bien les embeddings BGE.

FAISS n’est pas utilisé : plus complexe, moins flexible, inutile pour ce projet.  
ChromaDB est adapté aux usages locaux persistants et aux pipelines RAG avec stockage sur disque. [web:11][web:13][web:15][web:17][web:18]

### 2.4 Pipeline RAG correctif
Le pipeline suit 5 étapes :
1. Reformulation de la question (Gemma)
2. Recherche vectorielle dans Chroma (BGE)
3. Vérification de pertinence (Gemma)
4. Correction / relance si nécessaire
5. Réponse finale (Gemma)

Ce pipeline garantit :
- moins d’hallucinations,
- meilleure précision,
- meilleure cohérence,
- réponses basées uniquement sur les documents Markdown,
- un comportement plus fiable qu’un RAG simple.

### 2.5 Données sources
Le corpus est constitué de fichiers Markdown, organisés en modules pédagogiques.

Caractéristiques :
- stockage local,
- versionnable via GitHub (optionnel),
- aucun besoin de GitHub pour exécuter le RAG,
- structure simple et extensible.

## 3. Fonctionnement 100% offline
Une fois installé :
- pas besoin d’Internet,
- pas besoin de GitHub,
- pas besoin d’API externe,
- pas besoin de n8n.

Le système repose uniquement sur :
- LM Studio (Gemma + BGE),
- Python,
- ChromaDB,
- les fichiers Markdown locaux.

LM Studio permet un usage local et offline des modèles Gemma, sans dépendance à un service distant. [web:12][web:14]

## 4. Dépendances principales
- Python 3.10+
- llama-cpp-python (pour Gemma)
- chromadb (base vectorielle)
- BGE (embeddings GGUF via LM Studio)
- python-dotenv (optionnel)
- LM Studio (hébergement des modèles locaux)

## 5. Pourquoi ce choix d’architecture ?
### ✔️ Simplicité
Installation et maintenance faciles.

### ✔️ Robustesse
Pipeline correctif → moins d’erreurs, moins d’hallucinations.

### ✔️ Sécurité
Aucune donnée ne sort du Mac.

### ✔️ Coût
100% gratuit.

### ✔️ Performance
Gemma 12B + BGE + Chroma = excellent compromis  
→ rapide, fiable, cohérent, local.

## 6. Architecture générale du projet

```text
corpus_markdown/  →  ingest.py  →  ChromaDB  →  test_rag.py  →  rag_answer.py  →  Gemma 4
```

Étapes :
- Ingestion : lecture des fichiers Markdown + découpage en chunks
- Embeddings : conversion des chunks en vecteurs via BGE
- Stockage : insertion dans ChromaDB en mode persistant
- Retrieval : recherche sémantique dans ChromaDB
- Génération : réponse augmentée via Gemma 4

## Schéma ASCII — Architecture RAG Correctif

```text
Utilisateur
│
▼
Reformulation de la question (Gemma 4)
│
▼
Recherche vectorielle (BGE + ChromaDB)
│
▼
Vérification de pertinence (Gemma 4)
│
├── Si non pertinent → Reformulation + nouvelle recherche
│
▼
Réponse finale augmentée (Gemma 4)
```

## 7. Scripts du projet

### 7.1 `ingest.py` — Ingestion + Embeddings + Stockage
Fonctions :
- charge les fichiers Markdown,
- découpe en chunks,
- génère les embeddings via BGE,
- stocke dans ChromaDB en mode persistant.

Commande :

```bash
python ingest.py
```

### 7.2 `test_rag.py` — Test du retrieval
Fonctions :
- interroge ChromaDB,
- récupère les passages les plus pertinents,
- affiche les extraits.

Commande :

```bash
python test_rag.py
```

### 7.3 `rag_answer.py` — RAG complet
Fonctions :
- pose une question,
- récupère les passages pertinents,
- construit un prompt RAG,
- génère une réponse augmentée via Gemma 4.

Commande :

```bash
python rag_answer.py
```

## 8. Validation & Qualité

Ce projet RAG correctif a été conçu pour être fiable, reproductible et adapté aux besoins des PME/TPE.  
La validation du système repose sur trois niveaux de tests, documentés et exécutables.

### 8.1. Tests d’ingestion & embeddings
- Script : `ingest.py`
- Documentation : `tests/test_ingestion.md`
- Vérifie :
  - la lecture correcte des fichiers Markdown,
  - la génération des chunks,
  - la création des embeddings BGE,
  - la persistance des vecteurs dans ChromaDB.

### 8.2. Tests de recherche vectorielle (retrieval)
- Script : `test_rag.py`
- Documentation : `tests/test_retrieval.md`
- Vérifie :
  - la cohérence des passages retournés,
  - la pertinence sémantique,
  - l’intégrité de la base vectorielle.

### 8.3. Test du pipeline RAG complet
- Script : `rag_answer.py`
- Documentation : `tests/test_rag_complet.md`
- Vérifie :
  - la reformulation de la question,
  - la sélection des passages pertinents,
  - la correction éventuelle,
  - la réponse finale basée sur le corpus Markdown.

### 8.4. Test automatique global
- Script : `run_tests.py`
- Exécute automatiquement les trois étapes précédentes.
- Permet de valider rapidement que le système fonctionne sans erreur.

### 8.5. Approche PME/TPE
Cette stratégie de validation est volontairement simple, claire et reproductible.  
Elle garantit :
- un système fiable,
- une maintenance facile,
- une transparence totale pour le dirigeant,
- une qualité constante sans complexité inutile.

## 9. Arborescence du projet

```text
RAG-BLOCKCHAIN/
│
├── corpus_markdown/
│   ├── A1_definition.md
│   ├── A2_histoire.md
│   └── ...
│
├── chroma_db/                ← base vectorielle persistante
│
├── ingest.py                 ← ingestion + embeddings
├── test_rag.py               ← test retrieval
├── rag_answer.py             ← RAG complet
│
└── README.md             ← ce fichier
```

## 10. Ce que permet ce système
- Assistant blockchain offline
- Basé sur tes propres cours
- Recherche sémantique précise
- Réponses augmentées par ton corpus
- Sécurisé, local, sans cloud
- Extensible avec de nouveaux fichiers Markdown

Le recours à un stockage vectoriel persistant facilite la réutilisation du corpus et la séparation entre ingestion et interrogation. [web:11][web:13][web:15][web:17][web:18]

## 11. Prochaines évolutions possibles
- Interface web avec Gradio
- API locale avec FastAPI
- Mode conversationnel avec mémoire
- Ajout automatique de nouveaux documents
- Optimisation des embeddings

## 12. Conclusion
Ce projet fournit une base RAG locale, simple à maintenir et totalement autonome.  
En combinant un corpus Markdown, des embeddings locaux, ChromaDB persistant et un LLM local, tu obtiens un assistant blockchain privé, rapide, fiable et évolutif.
