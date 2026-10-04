import pandas as pd

df = pd.read_csv("sales_data_raw.csv")

# Check missing values and duplicates
print("Missing values before cleaning:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# Clean column names
df.columns = (df.columns.str.strip().str.lower()
              .str.replace(" ", "_")
              .str.replace("-", "_"))

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df["customer_name"] = df["customer_name"].fillna("Unknown").astype(str).str.strip().str.title()
df["gender"] = df["gender"].fillna("Unknown").astype(str).str.strip().str.lower()
df["gender"] = df["gender"].replace({"m": "male", "f": "female"})
df["city"] = df["city"].fillna("Unknown").astype(str).str.strip().str.title()

# Convert numeric columns
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["sales_amount"] = pd.to_numeric(df["sales_amount"], errors="coerce")

# Fill missing numeric values with median
df["quantity"] = df["quantity"].fillna(df["quantity"].median()).astype(int)
df["sales_amount"] = df["sales_amount"].fillna(df["sales_amount"].median())

# Standardize date format
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce").dt.strftime("%d-%m-%Y")

# Save
df.to_csv("sales_data_cleaned.csv", index=False)
print("Cleaning completed successfully.")
