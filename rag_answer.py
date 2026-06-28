import chromadb
from llama_cpp import Llama

# 1) Connexion à ChromaDB (persistant)
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("blockchain_rag")

# 2) Chargement du modèle Gemma 4 (LLM)
llm = Llama(
    model_path="/Users/claude/.lmstudio/models/gemma4-12b-Q4_0.gguf",  # adapte si besoin
    n_ctx=8192,
    n_threads=6
)

def rag_answer(query):
    # 3) Récupération des passages pertinents
    results = collection.query(
        query_texts=[query],
        n_results=4
    )

    contexts = "\n\n".join(results["documents"][0])

    # 4) Construction du prompt RAG
    prompt = f"""
Tu es un expert blockchain. Réponds de manière claire, structurée et pédagogique.

### Question
{query}

### Contexte issu de ma base de connaissances
{contexts}

### Réponse attendue
Explique en t'appuyant sur le contexte ci-dessus.
"""

    # 5) Génération avec Gemma 4
    output = llm(
        prompt,
        max_tokens=512,
        temperature=0.2,
        top_p=0.9
    )

    return output["choices"][0]["text"]

def main():
    query = "Explique le fonctionnement de la preuve de travail."
    answer = rag_answer(query)
    print("\n🧠 Réponse RAG :\n")
    print(answer)

if __name__ == "__main__":
    main()
