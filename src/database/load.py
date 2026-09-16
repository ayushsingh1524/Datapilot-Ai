from sqlalchemy import text

from src.database.connection import get_engine


def load_orders(df):

    engine = get_engine()

    with engine.begin() as connection:

        existing_ids = connection.execute(
            text("SELECT order_id FROM orders")
        ).fetchall()

        existing_ids = {row[0] for row in existing_ids}

    new_df = df[~df["order_id"].isin(existing_ids)].copy()

    if new_df.empty:
        print("No new records to load.")
        return

    new_df.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False,
        method="multi",
    )

    print(f"Loaded {len(new_df)} new records into PostgreSQL.")
    