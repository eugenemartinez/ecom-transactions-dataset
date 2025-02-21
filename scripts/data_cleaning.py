#!/usr/bin/env python
# coding: utf-8

# In[35]:


import os
import pandas as pd
import numpy as np

# Define the path to the "data" folder (one level up from "notebooks")
data_folder = os.path.join(os.path.dirname(os.getcwd()), "data")

# Define input and output file paths
input_file = os.path.join(data_folder, "ecom_transactions.csv")
output_file = os.path.join(data_folder, "cleaned_ecom_transactions.csv")

# Load dataset
df = pd.read_csv(input_file)

# Display the first few rows before cleaning
print("Before Cleaning:")
print(df.head())

### 1. HANDLE MISSING VALUES ###
# Convert 'Price' to numeric, setting errors to NaN
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Fill missing Prices with the median value
df.loc[:, "Price"] = df["Price"].fillna(df["Price"].median())

# Fill missing Product Categories with the most common one
df.loc[:, "Product Category"] = df["Product Category"].fillna(df["Product Category"].mode()[0])

# Convert 'Transaction Date' to datetime, forcing errors to NaT
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], errors="coerce")

# Convert 'Quantity' to integer (fill NaN with 1, assuming a single order)
df.loc[:, "Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(1).astype(int)

### 2. REMOVE DUPLICATES ###
df = df.drop_duplicates(subset=["Transaction ID"], keep="first")

### 3. HANDLE OUTLIERS ###
# Remove extreme outliers in Price (above 99th percentile)
upper_limit = df["Price"].quantile(0.99)
df = df[df["Price"] <= upper_limit]

# Remove extreme Quantity outliers (above 1000)
df = df[df["Quantity"] <= 1000]

### 4. FIX CATEGORICAL VALUES ###
# Standardize Product Category names (capitalize each word)
df.loc[:, "Product Category"] = df["Product Category"].str.title()

### 5. REMOVE INCORRECT VALUES ###
# Drop rows where Price or Quantity is negative
df = df[(df["Price"] > 0) & (df["Quantity"] > 0)]

# Fill missing Customer Ratings with the median value
df.loc[:, "Customer Rating"] = df["Customer Rating"].fillna(df["Customer Rating"].median())

# Fill missing Payment Methods with the most common one
df.loc[:, "Payment Method"] = df["Payment Method"].fillna(df["Payment Method"].mode()[0])

### 6. CHECK FOR BLANK VALUES ###
def check_blank_cells(df):
    """Checks for blank cells in the dataset and prints the results."""
    blank_counts = (df == "").sum() + (df == " ").sum()
    blank_columns = blank_counts[blank_counts > 0]
    
    if blank_columns.empty:
        print("\n✅ No blank cells found in the dataset.")
    else:
        from IPython.display import display  # Import for Jupyter display
        print("\n⚠️ Blank cells detected in the following columns:")
        display(blank_columns.to_frame(name="Blank Count"))  # Better display format

# Run the function on the cleaned DataFrame
check_blank_cells(df)

# Display cleaned dataset
print("\nAfter Cleaning:")
print(df.head())

# Save the cleaned dataset
df.to_csv(output_file, index=False)
print(f"\n✅ Data Cleaning Completed! Cleaned file saved at '{output_file}'")

