import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Loads the raw marketing A/B test CSV."""
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies the cleaning steps used throughout the analysis:
    - drops the unnamed index column from the CSV export
    - casts `converted` from bool to int (needed for statsmodels formulas)
    - adds a binary `treatment` column (1 = ad, 0 = psa)
    """
    df = df.drop(columns=["Unnamed: 0"])
    df["converted"] = df["converted"].astype(int)
    df["treatment"] = (df["test group"] == "ad").astype(int)
    return df