import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


def get_engine():

    host = os.getenv("DB_HOST", "127.0.0.1")
    port = os.getenv("DB_PORT", "5436")
    database = os.getenv("DB_NAME", "datapilot")
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD", "postgres")

    connection_url = (
        f"postgresql+psycopg2://{user}:{password}"
        f"@{host}:{port}/{database}"
    )

    return create_engine(connection_url)