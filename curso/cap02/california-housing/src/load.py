from pathlib import Path

import pandas as pd

DATA_PATH = Path("data/housing.csv")


def load_data() -> pd.DataFrame:
    """Load the housing dataset from a CSV file."""
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")
    return pd.read_csv(DATA_PATH)
