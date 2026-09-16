import pandas as pd


def profile_data(df: pd.DataFrame) -> dict:

    profile = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "data_types": df.dtypes.astype(str).to_dict(),
    }

    print("\nData Profile")
    print("-" * 30)
    print(f"Rows: {profile['rows']}")
    print(f"Columns: {profile['columns']}")
    print(f"Duplicate rows: {profile['duplicate_rows']}")
    print(f"Missing values: {profile['missing_values']}")

    return profile