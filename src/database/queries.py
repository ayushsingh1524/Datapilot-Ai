from sqlalchemy import text

from src.database.connection import get_engine


def execute_query(sql: str):
    engine = get_engine()

    with engine.connect() as connection:

        connection.execute(
            text("SET TRANSACTION READ ONLY")
        )

        connection.execute(
            text("SET LOCAL statement_timeout = '5000ms'")
        )

        result = connection.execute(text(sql))

        rows = result.mappings().fetchmany(100)

    return [dict(row) for row in rows]