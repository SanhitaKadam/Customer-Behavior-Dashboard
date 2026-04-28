import pandas as pd

# Load dataset
df = pd.read_csv("project_data.csv", encoding="latin1")
print(df.info())

# Convert dates
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['ShipDate'] = pd.to_datetime(df['ShipDate'])

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(0, inplace=True)

# Save cleaned file
df.to_csv("clean_data.csv", index=False)

print("Data Cleaned Successfully")

print(df.isnull().sum())
print(df.info())
print("Shape of Data set", df.shape)
