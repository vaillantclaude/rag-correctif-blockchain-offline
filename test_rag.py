import chromadb

# Connexion à ChromaDB
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("blockchain_rag")

# Exemple de question
query = "Comment fonctionne la preuve de travail dans la blockchain ?"

# Recherche sémantique
results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\n🔍 Résultats de la recherche :\n")
for doc in results["documents"][0]:
    print("—", doc[:300], "...\n")
