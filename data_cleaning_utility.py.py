# Data Cleaning Utility
import pandas as pd
import numpy as np

print("---- Data Cleaning Utility ----")

# 1️⃣ Create messy dataset (example)
data = {
    "Name ": ["Asha", "Ravi", "Ravi", "John", None],
    "Age": ["21", "22", "22", None, "20"],
    "Marks": [85, None, 90, 78, 88],
    "Date ": ["2024-01-01", "2024/02/01", "2024/02/01", "01-03-2024", None]
}

df = pd.DataFrame(data)
print("\nOriginal Data:\n", df)

log = []

# 2️⃣ Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
log.append("Column names standardized")

# 3️⃣ Handle missing values
missing_before = df.isnull().sum().sum()
df["age"] = df["age"].fillna(df["age"].mode()[0])
df["marks"] = df["marks"].fillna(df["marks"].mean())
df = df.dropna(subset=["name"])
missing_after = df.isnull().sum().sum()
log.append(f"Missing values handled ({missing_before} → {missing_after})")

# 4️⃣ Fix data types
df["age"] = df["age"].astype(int)
df["date"] = pd.to_datetime(df["date"], errors="coerce")
log.append("Data types corrected")

# 5️⃣ Remove duplicates
before_dup = len(df)
df = df.drop_duplicates()
after_dup = len(df)
log.append(f"Duplicates removed ({before_dup-after_dup})")

# 6️⃣ Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

# 7️⃣ Save cleaning log
with open("cleaning_log.txt", "w") as f:
    for item in log:
        f.write(item + "\n")

print("\nCleaned Data:\n", df)
print("\nCleaning log saved!")
