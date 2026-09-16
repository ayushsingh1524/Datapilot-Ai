import pandas as pd


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["product"] = df["product"].str.strip()
    df["category"] = df["category"].str.strip()
    df["region"] = df["region"].str.strip()
    df["payment_method"] = df["payment_method"].str.strip()

    df["price"] = pd.to_numeric(df["price"])
    df["quantity"] = pd.to_numeric(df["quantity"])
    df["order_date"] = pd.to_datetime(df["order_date"])

    df["total_amount"] = df["price"] * df["quantity"]

    print("Data transformation completed.")

    return df