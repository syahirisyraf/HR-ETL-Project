"""
Extract Module - Reads Data from source files
"""

import pandas as pd
from pathlib import Path

def extract_csv(file_path: str) -> pd.DataFrame:
    """
    Extract data from CSV file.

    Args:
        file_path: Path to the CSV file

    Returns: DataFrame with raw data
    """
    print(f"Extracting data from: {file_path}")

    #Check if file exists
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Read CSV
    df = pd.read_csv(file_path)

    print(f"[SUCCESS] Extracted {len(df)} rows and {len(df.columns)} columns")
    return df

if __name__ == "__main__":
    df = extract_csv("../dataset/Human Resource Data.csv")
    print(df.head())