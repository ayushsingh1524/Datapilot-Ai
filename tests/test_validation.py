import pandas as pd
import pytest

from src.validation.quality_checks import validate_orders


def test_valid_orders():
    df = pd.DataFrame({
        "order_id": [1],
        "customer_id": ["C001"],
        "product": ["Laptop"],
        "category": ["Electronics"],
        "price": [55000],
        "quantity": [1],
        "order_date": ["2026-09-01"],
        "region": ["Bengaluru"],
        "payment_method": ["UPI"],
    })

    validate_orders(df)


def test_duplicate_order_id():
    df = pd.DataFrame({
        "order_id": [1, 1],
        "customer_id": ["C001", "C002"],
        "product": ["Laptop", "Mouse"],
        "category": ["Electronics", "Electronics"],
        "price": [55000, 800],
        "quantity": [1, 2],
        "order_date": ["2026-09-01", "2026-09-01"],
        "region": ["Bengaluru", "Mumbai"],
        "payment_method": ["UPI", "Card"],
    })

    with pytest.raises(ValueError):
        validate_orders(df)