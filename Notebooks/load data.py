import pandas as pd
import os

# Get the main project folder path (Retail analysis)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build correct file paths
sales_path = os.path.join(BASE_DIR, "data", "sales_data.csv")
costs_path = os.path.join(BASE_DIR, "data", "product_costs.csv")

print("Looking for:", sales_path)
print("Looking for:", costs_path)

sales = pd.read_csv(sales_path)
costs = pd.read_csv(costs_path)

print("\nSALES DATA:")
print(sales.head())

print("\nCOST DATA:")
print(costs.head())
