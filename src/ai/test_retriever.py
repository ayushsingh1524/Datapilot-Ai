from src.ai.retriever import retrieve_relevant_schema


question = "Which product generated the highest revenue?"

results = retrieve_relevant_schema(question)

print("\nRelevant schema information:")
print("-" * 50)

for i, result in enumerate(results, start=1):
    print(f"\nResult {i}:")
    print(result)