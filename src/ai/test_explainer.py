from src.ai.explainer import explain_results


question = "What is the total revenue by product?"

results = [
    {"product": "Keyboard", "total_revenue": 7200.0},
    {"product": "Monitor", "total_revenue": 72000.0},
    {"product": "Mouse", "total_revenue": 16000.0},
    {"product": "Laptop", "total_revenue": 330000.0},
    {"product": "Headphones", "total_revenue": 15000.0},
]


explanation = explain_results(question, results)

print("\nAI Explanation:")
print(explanation)