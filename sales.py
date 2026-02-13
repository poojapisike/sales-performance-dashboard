import pandas as pd
df = pd.read_csv("superstore.csv", encoding="latin-1")

"""print("All columns in your dataset:")
for i, col in enumerate(df.columns):
    print(f"{i}: '{col}'")

print("\n" + "="*50)
print("First 3 rows:")
print(df.head(3))"""

"""print("Column names in your dataset:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())"""

total_revenue = df["Sales"].sum()

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()


growth = monthly_sales.pct_change() * 100

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

print(total_revenue)
print(growth)
print(top_products)
