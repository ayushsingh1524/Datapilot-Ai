import pandas as pd

from src.transformation.transform import transform_orders


def test_transform_orders():
    df = pd.DataFrame({
        "order_id": [1],
        "customer_id": ["C001"],
        "product": [" Laptop "],
        "category": [" Electronics "],
        "price": ["55000"],
        "quantity": ["2"],
        "order_date": ["2026-09-01"],
        "region": [" Bengaluru "],
        "payment_method": [" UPI "],
    })

    result = transform_orders(df)

    assert result["product"].iloc[0] == "Laptop"
    assert result["category"].iloc[0] == "Electronics"
    assert result["region"].iloc[0] == "Bengaluru"
    assert result["payment_method"].iloc[0] == "UPI"

    assert result["price"].iloc[0] == 55000
    assert result["quantity"].iloc[0] == 2
    assert result["total_amount"].iloc[0] == 110000