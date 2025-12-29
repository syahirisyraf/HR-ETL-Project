"""
ETL Pipeline Orchestrator
Coordinates Extract, Transform, and Load operations
"""
import sys
from datetime import datetime
from pathlib import Path

# Add src to path for imports
sys.path.append(str(Path(__file__).parent))

from extract import extract_csv
from transform import transform_data, get_data_quality_report
from load import load_to_supabase, verify_load


def run_etl_pipeline(source_file: str, table_name: str = 'employees') -> dict:
    """
    Run the complete ETL pipeline.
    
    Args:
        source_file: Path to source CSV file
        table_name: Target database table name
        
    Returns:
        Dictionary with pipeline execution results
    """
    print("=" * 60)
    print("HR ANALYTICS ETL PIPELINE")
    print(f"   Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    results = {
        'status': 'failed',
        'start_time': datetime.now(),
        'rows_extracted': 0,
        'rows_transformed': 0,
        'rows_loaded': 0
    }
    
    try:
        # EXTRACT
        print("\nPHASE 1: EXTRACT")
        print("-" * 40)
        df_raw = extract_csv(source_file)
        results['rows_extracted'] = len(df_raw)
        
        # TRANSFORM
        print("\nPHASE 2: TRANSFORM")
        print("-" * 40)
        df_clean = transform_data(df_raw)
        results['rows_transformed'] = len(df_clean)
        
        # Data Quality Report
        print("\nDATA QUALITY REPORT")
        print("-" * 40)
        quality_report = get_data_quality_report(df_clean)
        print(f"  Total Rows: {quality_report['total_rows']}")
        print(f"  Total Columns: {quality_report['total_columns']}")
        print(f"  Duplicate Rows: {quality_report['duplicates']}")
        
        # LOAD
        print("\nPHASE 3: LOAD")
        print("-" * 40)
        success = load_to_supabase(df_clean, table_name)
        
        if success:
            results['rows_loaded'] = verify_load(table_name)
            results['status'] = 'success'
        
    except Exception as e:
        print(f"\n[FAILED] Pipeline Error: {str(e)}")
        results['error'] = str(e)
    
    # Summary
    results['end_time'] = datetime.now()
    results['duration'] = (results['end_time'] - results['start_time']).total_seconds()
    
    print("\n" + "=" * 60)
    print("PIPELINE SUMMARY")
    print("=" * 60)
    print(f"  Status: {results['status'].upper()}")
    print(f"  Duration: {results['duration']:.2f} seconds")
    print(f"  Rows Extracted: {results['rows_extracted']}")
    print(f"  Rows Transformed: {results['rows_transformed']}")
    print(f"  Rows Loaded: {results['rows_loaded']}")
    print("=" * 60)
    
    return results


if __name__ == "__main__":
    source_file = "../dataset/Human Resource Data.csv"
    
    results = run_etl_pipeline(source_file)