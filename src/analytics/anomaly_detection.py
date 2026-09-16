import pandas as pd


def detect_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Detect unusual orders using IQR-based anomaly detection
    on total amount and quantity.
    """

    required_columns = {"total_amount", "quantity"}

    if not required_columns.issubset(df.columns):
        raise ValueError(
            "total_amount and quantity columns are required."
        )

    # IQR for total amount
    amount_q1 = df["total_amount"].quantile(0.25)
    amount_q3 = df["total_amount"].quantile(0.75)
    amount_iqr = amount_q3 - amount_q1

    amount_upper = amount_q3 + 1.5 * amount_iqr

    # IQR for quantity
    quantity_q1 = df["quantity"].quantile(0.25)
    quantity_q3 = df["quantity"].quantile(0.75)
    quantity_iqr = quantity_q3 - quantity_q1

    quantity_upper = quantity_q3 + 1.5 * quantity_iqr

    # Detect anomalies
    anomalies = df[
        (df["total_amount"] > amount_upper)
        | (df["quantity"] > quantity_upper)
    ].copy()

    return anomalies