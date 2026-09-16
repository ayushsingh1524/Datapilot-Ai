from fastapi import APIRouter

from src.ingestion.csv_loader import extract_orders
from src.transformation.transform import transform_orders
from src.analytics.anomaly_detection import detect_anomalies
from src.ai.anomaly_explainer import explain_anomalies


router = APIRouter()


@router.get("/anomalies")
def get_anomalies():

    df = extract_orders("data/raw/orders.csv")
    df = transform_orders(df)

    anomalies = detect_anomalies(df)

    anomaly_data = anomalies.to_dict(orient="records")

    try:
        if anomaly_data:
            explanation = explain_anomalies(anomaly_data)
        else:
            explanation = "No unusual orders were detected."

    except Exception:
        explanation = (
            "AI explanation is temporarily unavailable. "
            "The anomalies were detected using statistical analysis."
        )

    return {
        "count": len(anomalies),
        "anomalies": anomaly_data,
        "ai_explanation": explanation,
    }