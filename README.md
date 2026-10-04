# Data Analyst Internship - Task 1

## Data Cleaning and Preprocessing

This project completes Task 1 from the internship instructions.

### Objective
Clean and prepare a raw dataset containing common data-quality problems such as:
- Missing values
- Duplicate rows
- Inconsistent text formatting
- Inconsistent date formats
- Incorrect/inconsistent data types

### Tools
- Python
- Pandas
- Excel (cleaned CSV also provided as XLSX)

### Files
- `sales_data_raw.csv` - raw dataset before cleaning
- `sales_data_cleaned.csv` - final cleaned dataset
- `sales_data_cleaned.xlsx` - cleaned dataset for Excel
- `cleaning.py` - Python/Pandas cleaning code
- `summary.txt` - short summary of changes

### Cleaning steps
1. Checked missing values and duplicate rows.
2. Standardized column names.
3. Removed duplicate records.
4. Standardized gender and city values.
5. Converted numeric columns to numeric types.
6. Filled missing numeric values using the median.
7. Filled missing customer names with `Unknown`.
8. Standardized order dates to `dd-mm-yyyy`.
9. Performed final data-quality checks.

### How to run
```bash
pip install pandas openpyxl
python cleaning.py
```

The project is ready to upload as a GitHub repository for Task 1.
