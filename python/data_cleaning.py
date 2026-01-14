import pandas as pd

# Load data
df = pd.read_csv("../data/superstore_final_dataset.csv")

# Basic cleaning
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

if 'Row ID' in df.columns:
    df.drop(columns=['Row ID'], inplace=True)

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Save cleaned data
df.to_csv("../data/cleaned_superstore_sales.csv", index=False)

print("Dataset cleaned and ready for analysis")
