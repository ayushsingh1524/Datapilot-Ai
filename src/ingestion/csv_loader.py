import pandas as pd
from pathlib import Path


def extract_orders(file_path: str) -> pd.DataFrame:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("The input dataset is empty.")

    print(f"Extracted {len(df)} records from {file_path}")

    return df