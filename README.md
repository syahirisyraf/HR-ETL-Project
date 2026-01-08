# HR Analytics ETL Pipeline

A **simple ETL portfolio project** demonstrating data engineering fundamentals using Python, Supabase (PostgreSQL), and Power BI.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-green.svg)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)
![Portfolio](https://img.shields.io/badge/Portfolio-Project-orange.svg)

---

## 📋 Table of Contents

- [About This Project](#about-this-project)
- [Skills Demonstrated](#skills-demonstrated)
- [Architecture](#architecture)
- [Dataset](#dataset)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Power BI Dashboard](#power-bi-dashboard)
- [DAX Measures](#dax-measures)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 📖 About This Project

This is a **portfolio project** showcasing a simple end-to-end ETL pipeline. I built this to demonstrate my understanding of:

- How data flows from source to dashboard
- Data extraction, transformation, and loading processes
- Cloud database integration
- Data visualization and reporting

**Project Highlights:**
- Clean, well-commented Python code
- Cloud database using Supabase (free tier)
- Interactive Power BI dashboard
- Professional project structure

---

## 💼 Skills Demonstrated

| Skill | Description |
|-------|-------------|
| **Python** | ETL scripting with Pandas, SQLAlchemy |
| **SQL** | PostgreSQL database operations |
| **Cloud Database** | Supabase setup and connection |
| **Data Cleaning** | Handling nulls, parsing dates, formatting |
| **Data Visualization** | Power BI dashboards and DAX measures |
| **Version Control** | Git and GitHub |
| **Environment Management** | Virtual environments, .env files |

---

## 🏗️ Overview

This project demonstrates a complete ETL workflow:

1. **Extract** - Read raw HR data from CSV file
2. **Transform** - Clean, validate, and transform data using Python/Pandas
3. **Load** - Store processed data in Supabase (PostgreSQL cloud database)
4. **Visualize** - Create interactive dashboards in Power BI

---

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   CSV File  │────▶│   Python    │────▶│  Supabase   │────▶│  Power BI   │
│  (Source)   │     │  (ETL)      │     │ (PostgreSQL)│     │ (Dashboard) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
     EXTRACT          TRANSFORM            LOAD             VISUALIZE
```

---

## 📊 Dataset

The dataset contains **1,600 employee records** with **21 attributes**:

| Category | Columns |
|----------|---------|
| **Employee Info** | Emp_ID, Full_Name, Gender, DOB, Age |
| **Demographics** | Nationality, Ethnicity |
| **Job Details** | Job_Title, Department, Job_Level, Hire_Date, Status, Emp_Type |
| **Compensation** | Tenure (Years), Salary_Band, Salary |
| **Performance** | Job_Rating |
| **Location** | Location |
| **Attendance** | Days_Absent, Sick_Days, Annual_Leave |

---

## 🛠️ Technologies Used

All tools are **free** to use:

| Technology | Purpose | Cost |
|------------|---------|------|
| **Python 3.10+** | ETL scripting | Free |
| **Pandas** | Data manipulation | Free |
| **SQLAlchemy** | Database connection | Free |
| **psycopg2** | PostgreSQL adapter | Free |
| **Supabase** | Cloud PostgreSQL database | Free tier |
| **Power BI Desktop** | Data visualization | Free |

---

## 📁 Project Structure

```
HR-ETL-Project/
│
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
│
├── dataset/
│   └── Human Resource Data.csv    # Source data
│
├── src/
│   ├── extract.py        # Data extraction module
│   ├── transform.py      # Data transformation module
│   ├── load.py           # Data loading module
│   └── etl_pipeline.py   # Main ETL orchestrator
│
└── reports/
    └── HR_Dashboard.pbix # Power BI dashboard file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Power BI Desktop
- Supabase account (free tier)

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/HR-ETL-Project.git
cd HR-ETL-Project
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv etl_env

# Activate it
# Windows:
etl_env\Scripts\activate

# Mac/Linux:
source etl_env/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Supabase

1. Go to [https://supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Go to **Settings** → **Database** to get your connection details

### Step 5: Configure Environment Variables

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` with your Supabase credentials:
```env
SUPABASE_HOST=aws-0-xx-xxxx-x.pooler.supabase.com
SUPABASE_PORT=6543
SUPABASE_DB=postgres
SUPABASE_USER=postgres.xxxxxxxxxxxx
SUPABASE_PASSWORD=your_password_here
```

### Step 6: Run the ETL Pipeline

```bash
cd src
python etl_pipeline.py
```

**Expected Output:**
```
============================================================
🚀 HR ANALYTICS ETL PIPELINE
   Started: 2024-01-15 10:30:00
============================================================

📥 PHASE 1: EXTRACT
----------------------------------------
📂 Extracting data from: ../dataset/Human Resource Data.csv
✅ Extracted 1600 rows and 21 columns

🔄 PHASE 2: TRANSFORM
----------------------------------------
🔄 Starting data transformation...
  ✓ Column names standardized
  ✓ Dates parsed
  ✓ Salary cleaned
  ✓ Text fields cleaned
  ✓ Missing values handled
  ✓ Data validated
✅ Transformation complete: 1600 rows

📤 PHASE 3: LOAD
----------------------------------------
📤 Loading data to Supabase table: employees
  ✓ Database connection successful
✅ Successfully loaded 1600 rows to 'employees'

============================================================
📊 PIPELINE SUMMARY
============================================================
  Status: SUCCESS
  Duration: 3.45 seconds
  Rows Extracted: 1600
  Rows Transformed: 1600
  Rows Loaded: 1600
============================================================
```

---

## 📈 Power BI Dashboard

### Connecting Power BI to Supabase

1. Open **Power BI Desktop**
2. Click **Home** → **Get Data** → **PostgreSQL database**
3. Enter your Supabase connection details:
   - **Server:** `aws-0-xx-xxxx-x.pooler.supabase.com:6543`
   - **Database:** `postgres`
4. Select **Database** authentication and enter credentials
5. Select the `employees` table and click **Load**

### Dashboard Features

- **Total Employees** - Overall headcount
- **Active Employees** - Currently active staff
- **Average Salary** - Mean compensation
- **Turnover Rate** - Resignation/termination percentage
- **Department Breakdown** - Headcount by department
- **Status Distribution** - Active, Resigned, Retired, Terminated
- **Employment Type** - Full-time, Part-time, Other
- **Location Analysis** - Employees by country

---

## 📐 DAX Measures

```dax
// Total Employees
Total Employees = COUNTROWS(employees)

// Active Employees
Active Employees = 
CALCULATE(
    COUNTROWS(employees),
    employees[status] = "Active"
)

// Average Salary
Average Salary = 
FORMAT(
    AVERAGE(employees[salary]),
    "$#,##0"
)

// Turnover Count
Turnover Count = 
CALCULATE(
    COUNTROWS(employees),
    employees[status] IN {"Resigned", "Terminated"}
)

// Turnover Rate
Turnover Rate = 
FORMAT(
    DIVIDE(
        [Turnover Count],
        [Total Employees]
    ),
    "0.0%"
)

// Average Tenure
Average Tenure = 
FORMAT(
    AVERAGE(employees[tenure_years]),
    "0.0"
) & " years"

// Total Salary Cost
Total Salary Cost = 
FORMAT(
    SUM(employees[salary]),
    "$#,##0"
)

// Avg Job Rating
Avg Job Rating = 
FORMAT(
    AVERAGE(employees[job_rating]),
    "0.0"
)

// % of Total (for tables)
% of Total = 
FORMAT(
    DIVIDE(
        COUNTROWS(employees),
        CALCULATE(COUNTROWS(employees), ALL(employees))
    ),
    "0.0%"
)
```

---

## 📸 Screenshots

### ETL Pipeline Output
![ETL Pipeline](screenshots/etl_output.png)

### Power BI Dashboard
![Dashboard](screenshots/dashboard.png)

> **Note:** Add your own screenshots to the `screenshots/` folder

---

## 🤝 Contributing

Feel free to fork this project and make it your own! Suggestions and improvements are welcome.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

**Your Name** - [LinkedIn](https://linkedin.com/in/YOUR_LINKEDIN)

Project Link: [https://github.com/YOUR_USERNAME/HR-ETL-Project](https://github.com/YOUR_USERNAME/HR-ETL-Project)

---

## 🙏 Acknowledgments

- Sample HR Dataset for learning purposes
- [Supabase](https://supabase.com) - Free open source database
- [Power BI](https://powerbi.microsoft.com) - Free data visualization tool

---

## ⭐ Like This Project?

If you found this portfolio project helpful or interesting, please give it a **star**! ⭐

---

*A simple ETL portfolio project showcasing data engineering skills.*
