import pandas as pd

from src.analytics.anomaly_detection import detect_anomalies


def test_detect_anomalies():
    df = pd.DataFrame({
        "order_id": [1, 2, 3, 4, 5, 6, 7, 8],
        "total_amount": [100, 120, 110, 105, 115, 108, 125, 1000],
        "quantity": [1, 1, 1, 1, 1, 1, 1, 1],
    })

    result = detect_anomalies(df)

    assert len(result) == 1
    assert result.iloc[0]["order_id"] == 8