from src.ingestion.csv_loader import extract_orders
from src.transformation.transform import transform_orders
from src.analytics.anomaly_detection import detect_anomalies
from src.ai.anomaly_explainer import explain_anomalies


df = extract_orders("data/raw/orders.csv")
df = transform_orders(df)

anomalies = detect_anomalies(df)

anomaly_data = anomalies.to_dict(orient="records")

explanation = explain_anomalies(anomaly_data)

print("\nAI Anomaly Explanation:")
print("-" * 40)
print(explanation)
