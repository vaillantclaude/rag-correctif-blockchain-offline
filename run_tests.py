import subprocess

def run_command(label, command):
    print(f"\n=== {label} ===")
    try:
        subprocess.run(command, check=True)
        print(f"[OK] {label} exécuté sans erreur.")
    except subprocess.CalledProcessError as e:
        print(f"[ERREUR] {label} a échoué.")
        print(e)
        raise

if __name__ == "__main__":
    print("Lancement des tests du pipeline RAG correctif...\n")

    # Test ingestion & embeddings
    run_command("Test ingestion & embeddings", ["python3", "ingest.py"])

    # Test retrieval (recherche vectorielle)
    run_command("Test retrieval (recherche vectorielle)", ["python3", "test_rag.py"])

    # Test RAG complet
    run_command("Test RAG complet", ["python3", "rag_answer.py"])

    print("\n✔️ Tous les tests ont été exécutés.")
