import pandas as pd

# Load data
df = pd.read_csv("../data/superstore_final_dataset.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Drop technical identifier column
if 'Row_ID' in df.columns:
    df.drop(columns=['Row_ID'], inplace=True)

# Convert date columns (day first)
df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)

# Create time-based feature
df['order_month'] = df['Order_Date'].dt.to_period('M')
df['sales_bucket'] = pd.cut(
    df['Sales'],
    bins=[0, 100, 500, 1000, 5000, df['Sales'].max()],
    labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']
)

# Save cleaned dataset
df.to_csv("../data/cleaned_superstore_sales.csv", index=False)

print("Dataset cleaned and ready for analysis")