import pandas as pd
import os

# Load data
data = pd.read_excel(os.path.join('data', 'feedback.xlsx'))

# Print column names to debug
print("Columns in the dataset:", data.columns)

# Print the first few rows of the dataset to inspect the data
print("First few rows of the dataset:")
print(data.head())
