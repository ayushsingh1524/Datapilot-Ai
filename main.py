from src.ingestion.csv_loader import extract_orders
from src.validation.quality_checks import validate_orders
from src.validation.profiler import profile_data
from src.transformation.transform import transform_orders
from src.database.load import load_orders


def main():

    print("Starting DataPilot ETL pipeline...")

    df = extract_orders("data/raw/orders.csv")

    profile_data(df)

    validate_orders(df)

    df = transform_orders(df)

    load_orders(df)

    print("DataPilot ETL pipeline completed successfully.")


if __name__ == "__main__":
    main()