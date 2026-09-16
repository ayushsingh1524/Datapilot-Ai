from src.ai.schema_documents import SCHEMA_DOCUMENTS
from src.ai.vector_store import store_schema_embedding


def main():
    print("Indexing schema documents...")

    for document in SCHEMA_DOCUMENTS:
        store_schema_embedding(document)

    print(f"Indexed {len(SCHEMA_DOCUMENTS)} schema documents.")
    print("Schema indexing completed successfully.")


if __name__ == "__main__":
    main()
