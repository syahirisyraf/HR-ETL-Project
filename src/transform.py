"""
Transform Module - Cleans and transforms data
"""
import pandas as pd
import numpy as np


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names to snake_case."""
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(' ', '_')
        .str.replace('(', '')
        .str.replace(')', '')
    )
    return df


def clean_salary(salary_str: str) -> float:
    """Convert salary string to float."""
    if pd.isna(salary_str):
        return None
    # Remove $, commas, and convert to float
    cleaned = str(salary_str).replace('$', '').replace(',', '').strip()
    try:
        return float(cleaned)
    except ValueError:
        return None


def parse_date(date_str: str) -> pd.Timestamp:
    """Parse date in DD/MM/YYYY format."""
    if pd.isna(date_str):
        return None
    try:
        return pd.to_datetime(date_str, format='%d/%m/%Y')
    except:
        return None


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Main transformation function.
    
    Transformations applied:
    1. Clean column names
    2. Parse dates (DOB, Hire_Date)
    3. Clean salary (remove $ and commas)
    4. Handle missing values
    5. Standardize text fields
    6. Add calculated fields
    """
    print("[PROCESSING] Starting data transformation...")
    
    # Create a copy to avoid modifying original
    df = df.copy()
    
    # 1. Clean column names
    df = clean_column_names(df)
    print("  ✓ Column names standardized")
    
    # 2. Parse dates
    df['dob'] = df['dob'].apply(parse_date)
    df['hire_date'] = df['hire_date'].apply(parse_date)
    print("  ✓ Dates parsed")
    
    # 3. Clean salary
    df['salary'] = df['salary'].apply(clean_salary)
    print("  ✓ Salary cleaned")
    
    # 4. Clean text fields - strip whitespace and standardize
    text_columns = ['full_name', 'gender', 'nationality', 'ethnicity', 
                    'job_title', 'department', 'job_level', 'status', 
                    'emp_type', 'salary_band', 'location']
    
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].str.strip()
    print("  ✓ Text fields cleaned")
    
    # 5. Handle missing values
    # Fill numeric NaN with 0 for leave/absence columns
    leave_columns = ['days_absent', 'sick_days', 'annual_leave']
    for col in leave_columns:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)
    print("  ✓ Missing values handled")
    
    # 6. Data validation
    # Ensure age is reasonable
    df = df[(df['age'] >= 18) & (df['age'] <= 100)]
    
    # Ensure salary is positive
    df = df[df['salary'] > 0]
    print("  ✓ Data validated")
    
    # 7. Rename columns to match database schema
    column_mapping = {
        'tenure_years': 'tenure_years'  # Already correct after cleaning
    }
    
    print(f"[SUCCESS] Transformation complete: {len(df)} rows")
    return df


def get_data_quality_report(df: pd.DataFrame) -> dict:
    """Generate a data quality report."""
    report = {
        'total_rows': len(df),
        'total_columns': len(df.columns),
        'missing_values': df.isnull().sum().to_dict(),
        'duplicates': df.duplicated().sum(),
        'data_types': df.dtypes.astype(str).to_dict()
    }
    return report


if __name__ == "__main__":
    # Test transformation
    from extract import extract_csv
    
    df = extract_csv("../dataset/Human Resource Data.csv")
    df_transformed = transform_data(df)
    
    print("\nData Quality Report:")
    report = get_data_quality_report(df_transformed)
    print(f"  Rows: {report['total_rows']}")
    print(f"  Duplicates: {report['duplicates']}")