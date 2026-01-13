import pandas as pd
df = pd.read_csv(r"rawdata\rawdata.csv")
print(df.head())
print(df.info())
print(df.isnull().sum())
# Convert Age to numeric
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Replace unrealistic ages
df.loc[(df["Age"] < 16) | (df["Age"] > 100), "Age"] = df["Age"].median()
df["Gender"] = df["Gender"].replace({
    "Male": "M",
    "Female": "F",
    "male": "M",
    "female": "F"
})
df["Quantity"] = df["Quantity"].replace({"three": 3})
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
df["Customer Name"] = df["Customer Name"].fillna("Unknown Customer")
df["City"] = df["City"].fillna("Unknown City")

df.drop_duplicates(inplace=True)
df.drop_duplicates(inplace=True)

print("Clean file saved successfully!")
print("\n=== BASIC BUSINESS INSIGHTS ===")
# Total revenue
df["Revenue"] = df["Quantity"] * df["Unit Price"]

print("Total Revenue:", df["Revenue"].sum())
# Revenue by city
print("\nRevenue by City:")
print(df.groupby("City")["Revenue"].sum())
# Save FINAL clean file (ONLY ONE SAVE)
df.to_csv("clean_retail_sales.csv", index=False)
# Best selling products
print("\nTop Products:")
print(df.groupby("Product")["Quantity"].sum().sort_values(ascending=False))
# Payment method usage
print("\nPayment Method Usage:")
print(df["Payment Method"].value_counts())

