import os
import chromadb
from llama_cpp import Llama

# Dossier contenant tes fichiers Markdown
CORPUS_DIR = "corpus_markdown"

# Initialisation de ChromaDB (stockage local)
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("blockchain_rag")

# Chargement du modèle d'embeddings local (GGUF)
embed_model = Llama(
    model_path="/Users/claude/.lmstudio/models/CompendiumLabs/bge-small-en-v1.5-gguf/bge-small-en-v1.5-q8_0.gguf",
    embedding=True
)

def embed_text(texts):
    vectors = []
    for t in texts:
        output = embed_model.embed(t)
        vectors.append(output)
    return vectors

def load_markdown_files():
    docs = []
    for root, _, files in os.walk(CORPUS_DIR):
        for f in files:
            if f.endswith(".md"):
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as file:
                    docs.append((path, file.read()))
    return docs

def chunk_text(text, chunk_size=800, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def main():
    docs = load_markdown_files()
    print(f"Documents trouvés : {len(docs)}")

    all_chunks = []
    all_ids = []

    for idx, (path, content) in enumerate(docs):
        chunks = chunk_text(content)
        print(f"{path} → {len(chunks)} chunks")

        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            all_ids.append(f"{idx}_{i}")

    print(f"Total chunks : {len(all_chunks)}")

    # Génération des embeddings offline
    print("Génération des embeddings (offline)...")
    embeddings = embed_text(all_chunks)

    # Ajout dans Chroma
    print("Ajout dans ChromaDB...")
    collection.add(
        ids=all_ids,
        documents=all_chunks,
        embeddings=embeddings
    )

    print("Ingestion terminée ✔️")

if __name__ == "__main__":
    main()
