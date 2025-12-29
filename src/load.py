"""
Load Module - Loads data into Supabase (PostgreSQL)
"""

import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_connection_string() -> str:
    """Build PostgreSQL connection string from environment variables."""
    host = os.getenv('SUPABASE_HOST')
    port = os.getenv('SUPABASE_PORT', '5432')
    db = os.getenv('SUPABASE_DB', 'postgres')
    user = os.getenv('SUPABASE_USER', 'postgres')
    password = os.getenv('SUPABASE_PASSWORD')
    
    return f"postgresql://{user}:{password}@{host}:{port}/{db}"

def create_db_engine():
    """Create SQLAlchemy engine for database connection."""
    connection_string = get_connection_string()
    engine = create_engine(connection_string)
    return engine

def load_to_supabase(
        df: pd.DataFrame,
        table_name: str = 'employees',
        if_exists: str = 'replace'
) -> bool:
    """
    Load DataFrame to Supabase PostgreSQL database.
    
    Args:
        df: DataFrame to load
        table_name: Target table name
        if_exists: How to handle existing table ('replace', 'append', 'fail')
        
    Returns:
        True if successful, False otherwise
    """
    print(f"[PROCESSING] Loading data to Supabase table: {table_name}")

    try:
        engine = create_db_engine()

        # Test Connection
        with engine.connect() as conn:
            result = conn.execute(text("SELCT 1"))
            print("Database Connection SUCCESSFUL")

        # Load data
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists=if_exists,
            index=False,
            chunksize=500 # Load in chunks for large datasets
        )

        print(f"[SUCCESS] Sucessfully loaded {len(df)} rows to '{table_name}")
        return True

    except Exception as e:
        print(f"[FAILED] Error loading data: {str(e)}")
        return False
    
def verify_load(table_name: str = 'employees') -> int:
    """Verify data was loaded by counting rows."""
    try:
        engine = create_db_engine()
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            count = result.scalar()
            print(f"Verification: {count} rows in '{table_name}'")
            return count

    except Exception as e:
        print(f"[FAILED!!!] Verification error: {str(e)}")
        return -1
    
if __name__ == "__main__":
    # Test connection
    engine = create_db_engine()
    print("Testing connection...")
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version()"))
            print(f"Connected to: {result.scalar()}")
    except Exception as e:
        print(f"Connection failed: {e}")