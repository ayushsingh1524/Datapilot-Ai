from src.ai.retriever import retrieve_relevant_schema


def main():
    question = "Which product generated the highest revenue?"

    print("User question:")
    print(question)

    print("\nRetrieving relevant knowledge...")
    knowledge = retrieve_relevant_schema(question)

    print("\nRAG Context:")
    print("-" * 50)

    for item in knowledge:
        print(item)
        print("-" * 50)


if __name__ == "__main__":
    main()
    