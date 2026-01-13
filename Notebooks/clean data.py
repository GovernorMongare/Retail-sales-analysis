import pandas as pd

# Load data

BASE = r"C:\Users\Admin\Desktop\Retail analysis\data"

sales = pd.read_csv(BASE + r"\sales_data.csv")
costs = pd.read_csv(BASE + r"\product_costs.csv")

# Merge cost into sales
df = sales.merge(costs, on="Product", how="left")

# Clean column names
df.columns = df.columns.str.strip()

# Create Revenue and Profit
df["Revenue"] = df["Quantity"] * df["Unit Price"]
df["Cost"] = df["Quantity"] * df["Cost Price"]
df["Profit"] = df["Revenue"] - df["Cost"]

# Save clean data for Power BI
df.to_csv("../data/clean_retail_data.csv", index=False)

print("Clean data created successfully!")
print(df.head())


