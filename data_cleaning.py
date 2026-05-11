import pandas as pd

# Load dataset
df = pd.read_csv("customer_data.csv")

# Remove missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)

print("Data cleaning completed")
