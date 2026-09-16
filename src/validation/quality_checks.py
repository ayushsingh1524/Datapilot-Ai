import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "customer_id",
    "product",
    "category",
    "price",
    "quantity",
    "order_date",
    "region",
    "payment_method",
}


def validate_orders(df: pd.DataFrame) -> None:

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    if df["order_id"].isnull().any():
        raise ValueError("order_id cannot contain null values.")

    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order_id values detected.")

    if df["product"].isnull().any():
        raise ValueError("Product cannot contain null values.")

    if (df["price"] <= 0).any():
        raise ValueError("Price must be greater than zero.")

    if (df["quantity"] <= 0).any():
        raise ValueError("Quantity must be greater than zero.")

    print("Data validation passed.")