#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd
import numpy as np
import random
from faker import Faker

# Define the path to the "data" folder (one level up from "notebooks")
data_folder = os.path.join(os.path.dirname(os.getcwd()), "data")

# Ensure the "data" folder exists
os.makedirs(data_folder, exist_ok=True)

# Initialize Faker instance
fake = Faker()

# Define number of rows
num_rows = 1000

# Generate dataset
data = {
    "Transaction ID": [fake.uuid4() for _ in range(num_rows)],
    "Customer ID": [fake.uuid4() for _ in range(num_rows)],
    "Transaction Date": [fake.date_between(start_date="-2y", end_date="today") for _ in range(num_rows)],
    "Product Category": [random.choice(["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"]) for _ in range(num_rows)],
    "Price": [round(random.uniform(5, 500), 2) for _ in range(num_rows)],
    "Quantity": [random.randint(1, 5) for _ in range(num_rows)],
    "Payment Method": [random.choice(["Credit Card", "Debit Card", "PayPal", "Gift Card", "Crypto"]) for _ in range(num_rows)],
    "Shipping Status": [random.choice(["Shipped", "Pending", "Delivered", "Cancelled"]) for _ in range(num_rows)],
    "Customer Rating": [random.choice([1, 2, 3, 4, 5, np.nan]) for _ in range(num_rows)]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Introduce missing values in some columns
for col in ["Price", "Quantity", "Payment Method", "Customer Rating"]:
    df.loc[df.sample(frac=0.05).index, col] = np.nan  # 5% missing data

# Cast Price column to object to handle mixed types
df["Price"] = df["Price"].astype(object)

# Introduce data errors
for row in df.sample(frac=0.02).index:  # 2% erroneous data
    df.at[row, "Price"] = "ERROR"  # Inject string in numeric field

# Save the dataset in the "data" folder
file_path = os.path.join(data_folder, "ecom_transactions.csv")
df.to_csv(file_path, index=False)

print(f"✅ Dataset generated successfully! Saved at '{file_path}'")

