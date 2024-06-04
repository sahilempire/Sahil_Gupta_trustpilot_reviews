# File: inspect_columns.py

import pandas as pd

# Load data
data = pd.read_excel(r"data/Feedback.xlsx")

# Print column names to inspect
print(data.columns)
