#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Ensure visualizations directory exists
os.makedirs("../visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv("../data/cleaned_ecom_transactions.csv")

# Display first few rows
df.head()


# In[4]:


# Set figure size for better visibility
plt.figure(figsize=(10, 6))

# Create a bar chart showing transaction count per product category
sns.barplot(x=df["Product Category"].value_counts().index, 
            y=df["Product Category"].value_counts().values, 
            palette="viridis")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add labels and title
plt.xlabel("Product Category")
plt.ylabel("Number of Transactions")
plt.title("Sales Distribution by Product Category")

# Save the plot as an image
plt.savefig("../visualizations/sales_by_category.png")

# Show the plot
plt.show()


# In[9]:


# Convert transaction date to datetime format for time-series analysis
df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])

# Group transactions by month and count occurrences
df_trend = df.groupby(df["Transaction Date"].dt.to_period("M")).size()

# Set figure size
plt.figure(figsize=(12, 6))

# Plot the sales trend over time with a more pleasing color
df_trend.plot(kind="line", marker="o", color="#2a9d8f", linestyle="-", linewidth=2, markersize=6)

# Add labels and title
plt.xlabel("Date", fontsize=12, fontweight="bold")
plt.ylabel("Number of Transactions", fontsize=12, fontweight="bold")
plt.title("Sales Trend Over Time", fontsize=14, fontweight="bold")

# Save the plot as an image
plt.savefig("../visualizations/sales_trend.png", dpi=300, bbox_inches="tight")

# Show the plot
plt.show()


# In[10]:


# Set figure size
plt.figure(figsize=(8, 8))

# Create a pie chart showing payment method distribution
df["Payment Method"].value_counts().plot(kind="pie", 
                                         autopct="%1.1f%%", 
                                         startangle=90, 
                                         colormap="Pastel1")

# Set title
plt.title("Distribution of Payment Methods")

# Remove default y-label for a cleaner look
plt.ylabel("")

# Save the plot as an image
plt.savefig("../visualizations/payment_methods.png")

# Show the plot
plt.show()


# In[11]:


# Set figure size
plt.figure(figsize=(10, 6))

# Create a histogram with Kernel Density Estimate (KDE) for price distribution
sns.histplot(df["Price"], bins=30, kde=True, color="c")

# Add labels and title
plt.xlabel("Price ($)")
plt.ylabel("Count")
plt.title("Distribution of Product Prices")

# Save the plot as an image
plt.savefig("../visualizations/price_distribution.png")

# Show the plot
plt.show()


# In[7]:


# Set figure size
plt.figure(figsize=(8, 6))

# Create a count plot for shipping status with explicit hue assignment
sns.countplot(x=df["Shipping Status"], hue=df["Shipping Status"], palette="Set2", legend=False)

# Add labels and title
plt.xlabel("Shipping Status")
plt.ylabel("Count")
plt.title("Order Shipping Status Breakdown")

# Save the plot as an image
plt.savefig("../visualizations/shipping_status.png")

# Show the plot
plt.show()

