# HR Analytics ETL Pipeline

## 🎯 Project Overview
End-to-end ETL pipeline for HR analytics using Python, Supabase, and Power BI.

## 🏗️ Architecture
- **Extract:** Python/Pandas reads CSV data
- **Transform:** Data cleaning, validation, type conversion
- **Load:** SQLAlchemy loads to Supabase PostgreSQL
- **Visualize:** Power BI dashboards

## 🛠️ Technologies
- Python 3.10+
- Pandas
- SQLAlchemy
- Supabase (PostgreSQL)
- Power BI

## 📊 Dataset
- 1,600 employee records
- 21 attributes including demographics, compensation, performance

## 🚀 Quick Start
1. Clone repository
2. Set up `.env` with Supabase credentials
3. Run `python src/etl_pipeline.py`
4. Connect Power BI to Supabase

## 📈 Dashboard Features
- Executive KPIs
- Demographic analysis
- Compensation insights
- Performance metrics