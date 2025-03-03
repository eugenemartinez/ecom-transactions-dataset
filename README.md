# E-Commerce Transactions Dataset

## Overview
This project provides a synthetic dataset of e-commerce transactions, along with scripts and notebooks for data generation, cleaning, and visualization. It simulates real-world sales data to demonstrate data analysis techniques, data preprocessing, and visualization.

## Project Structure
```
ecom-transactions-dataset
├── data
│   ├── cleaned_ecom_transactions.csv
│   ├── ecom_transactions.csv
├── notebook
│   ├── data_cleaning.ipynb
│   ├── data_generation.ipynb
│   ├── data_visualization.ipynb
├── scripts
│   ├── data_cleaning.py
│   ├── data_generation.py
│   ├── data_visualization.py
├── visualizations
│   ├── payment_methods.png
│   ├── price_distribution.png
│   ├── sales_by_category.png
│   ├── sales_trend.png
│   ├── shipping_status.png
├── README.md
```

## Data Generation
The dataset is generated using Python with the `Faker` and `NumPy` libraries to create realistic transaction data. The dataset consists of 1,000 rows with fields including:
- Transaction ID
- Customer ID
- Transaction Date
- Product Category
- Price
- Quantity
- Payment Method
- Shipping Status
- Customer Rating

### Key Features of Data Generation
- **Randomized transaction data**: Ensures variation in each row.
- **Missing values**: Introduced in certain columns to simulate real-world data issues.
- **Erroneous data**: Injects inconsistencies, such as incorrect data types, for data cleaning demonstration.

## Data Cleaning Process
The dataset undergoes a structured cleaning process to ensure data consistency and accuracy:

1. **Handling Missing Values**
   - Converts `Price` to numeric, replacing errors with NaN.
   - Fills missing `Product Category` values with the most common category.
   - Converts `Transaction Date` to datetime format.
   - Uses linear regression to estimate missing `Price` values based on `Quantity`.
   
2. **Removing Duplicates**
   - Drops duplicate `Transaction ID` entries.

3. **Handling Outliers**
   - Removes extreme outliers in `Price` above the 99th percentile.
   - Removes unrealistic `Quantity` values over 1000.

4. **Fixing Categorical Values**
   - Standardizes `Product Category` names.

5. **Removing Incorrect Values**
   - Drops negative values for `Price` and `Quantity`.
   - Fills missing `Customer Rating` with the median value.
   - Replaces missing `Payment Method` values with the most common method.

## Data Visualizations

### Sales Trend Over Time
![Sales Trend](visualizations/sales_trend.png)
**Interpretation:** This line chart shows the number of transactions per month. The trend provides insights into seasonality and fluctuations in e-commerce activity. Spikes may indicate promotional periods or holiday seasons, while dips may correspond to off-peak periods.

### Sales by Product Category
![Sales by Category](visualizations/sales_by_category.png)
**Interpretation:** This chart shows the distribution of transactions across different product categories. Categories with higher transaction counts indicate popular product segments, which can help businesses focus their marketing efforts.

### Price Distribution
![Price Distribution](visualizations/price_distribution.png)
**Interpretation:** This histogram highlights the frequency of different price points in the dataset. A skewed distribution may suggest that certain price ranges are more common in transactions, influencing pricing strategies.

### Shipping Status Distribution
![Shipping Status](visualizations/shipping_status.png)
**Interpretation:** This chart presents the breakdown of shipping statuses. A high number of cancelled orders may indicate customer dissatisfaction or logistical issues, whereas a high rate of successful deliveries suggests smooth order fulfillment.

### Payment Method Distribution
![Payment Methods](visualizations/payment_methods.png)
**Interpretation:** This chart visualizes the popularity of different payment methods. Understanding payment preferences can help optimize checkout experiences and inform business decisions on which payment options to offer. The most used payment method is debit cards, while the least used is gift cards.

## How to Use
1. **Generate Data:** Run `scripts/data_generation.py` to create a synthetic dataset.
2. **Clean Data:** Use `scripts/data_cleaning.py` to preprocess the dataset.
3. **Visualize Data:** Run `scripts/data_visualization.py` to generate insights.
4. **Explore Notebooks:** Open `notebook/` to review detailed analysis steps.

## License
This project is open-source and can be freely used for learning and experimentation.

## Acknowledgments
- `Faker` for generating realistic synthetic data.
- `Seaborn` and `Matplotlib` for data visualization.
- `pandas` and `NumPy` for data manipulation.

This repository provides a structured approach to working with e-commerce transaction data, covering data generation, cleaning, and visualization techniques.