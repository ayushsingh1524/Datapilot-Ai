from fastapi import APIRouter
from sqlalchemy import text

from src.database.connection import get_engine

router = APIRouter()


# -------------------------
# Overall Summary
# -------------------------

@router.get("/summary")
def get_summary():
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    COUNT(*) AS total_orders,
                    SUM(total_amount) AS total_revenue,
                    ROUND(AVG(total_amount), 2) AS average_order_value
                FROM orders
            """)
        ).mappings().first()

    return dict(result)


# -------------------------
# Revenue by Product
# -------------------------

@router.get("/products")
def get_product_revenue():
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    product,
                    SUM(total_amount) AS revenue
                FROM orders
                GROUP BY product
                ORDER BY revenue DESC
            """)
        ).mappings().all()

    return [dict(row) for row in result]


# -------------------------
# Revenue by Region
# -------------------------

@router.get("/regions")
def get_region_revenue():
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    region,
                    SUM(total_amount) AS revenue
                FROM orders
                GROUP BY region
                ORDER BY revenue DESC
            """)
        ).mappings().all()

    return [dict(row) for row in result]


# -------------------------
# Daily Revenue
# -------------------------

@router.get("/daily")
def get_daily_revenue():
    engine = get_engine()

    with engine.connect() as connection:
        result = connection.execute(
            text("""
                SELECT
                    order_date,
                    SUM(total_amount) AS revenue
                FROM orders
                GROUP BY order_date
                ORDER BY order_date
            """)
        ).mappings().all()

    return [dict(row) for row in result]