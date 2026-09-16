from sqlalchemy import inspect

from src.database.connection import get_engine


def get_database_schema() -> str:
    engine = get_engine()

    inspector = inspect(engine)

    tables = inspector.get_table_names()

    schema_parts = []

    for table in tables:
        columns = inspector.get_columns(table)

        schema_parts.append(f"Table: {table}")

        for column in columns:
            column_name = column["name"]
            column_type = str(column["type"])

            schema_parts.append(
                f"- {column_name}: {column_type}"
            )

        schema_parts.append("")

    return "\n".join(schema_parts)
