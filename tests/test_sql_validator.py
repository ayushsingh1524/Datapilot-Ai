import pytest

from src.ai.sql_validator import validate_sql


def test_valid_select():
    sql = "SELECT * FROM orders"

    result = validate_sql(sql)

    assert result == sql


def test_reject_delete():
    with pytest.raises(ValueError):
        validate_sql("DELETE FROM orders")


def test_reject_update():
    with pytest.raises(ValueError):
        validate_sql("UPDATE orders SET quantity = 10")


def test_reject_drop():
    with pytest.raises(ValueError):
        validate_sql("DROP TABLE orders")


def test_reject_multiple_statements():
    with pytest.raises(ValueError):
        validate_sql("SELECT * FROM orders; DELETE FROM orders")
def test_valid_with_query():
    sql = """
    WITH product_sales AS (
        SELECT product, SUM(total_amount) AS revenue
        FROM orders
        GROUP BY product
    )
    SELECT *
    FROM product_sales
    """

    result = validate_sql(sql)

    assert result.startswith("WITH")