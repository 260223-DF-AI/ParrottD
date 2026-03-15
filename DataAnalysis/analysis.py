#Data Loading and Exploration
import numpy as np
import pandas as pd
def load_data(filepath):
    """
    Load the orders dataset.
    - Parse dates correctly
    - Handle missing values
    - Return a clean DataFrame
    """
    data = pd.read_csv(filepath)
    cleaned_data = clean_data(data)

    return cleaned_data

def explore_data(df):
    """
    Print basic statistics about the dataset:
    - Shape (rows, columns)
    - Data types
    - Missing value counts
    - Basic statistics for numeric columns
    - Date range covered
    """
    pass

# Data Cleaning and Transformation
def clean_data(df):
    """
    Clean the dataset:
    - Remove duplicates
    - Fill or drop missing values (document your strategy)
    - Standardize text columns (strip whitespace, consistent case)
    - Add calculated columns: 'total_amount' = quantity * unit_price
    """
    df.drop_duplicates(inplace=True)
    df = df.dropna()
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
    text_cols = ["region", "category", "product_name"]
    df[text_cols] = df[text_cols].apply(lambda col: col.str.title())
    df['quantity'] = df['quantity'].astype(int)
    df['unit_price'] = df['unit_price'].astype(float)
    df['order_date'] = pd.to_datetime(df['order_date'])
    df['total_amount'] = df['quantity'] * df['unit_price']
    return df

def add_time_features(df):
    """
    Add time-based features:
    - day_of_week (0=Monday, 6=Sunday)
    - month
    - quarter
    - is_weekend (boolean)
    """
# Analysis Functions
def sales_by_category(df):
    """
    Calculate total sales and order count by category.
    Returns: DataFrame with columns [category, total_sales, order_count, avg_order_value]
    Sorted by total_sales descending.
    """
    categories = df.groupby("category")
    total_sales = categories['quantity'].sum()
    order_count = categories.size()
    avg_order_value = categories['total_amount']/categories['order_count']
    pass

def sales_by_region(df):
    """
    Calculate total sales by region.
    Returns: DataFrame with columns [region, total_sales, percentage_of_total]
    """
    pass

def top_products(df, n=10):
    """
    Find top N products by total sales.
    Returns: DataFrame with columns [product_name, category, total_sales, units_sold]
    """
    pass

def daily_sales_trend(df):
    """
    Calculate daily sales totals.
    Returns: DataFrame with columns [date, total_sales, order_count]
    """
    pass

def customer_analysis(df):
    """
    Analyze customer purchasing behavior.
    Returns: DataFrame with columns [customer_id, total_spent, order_count,
             avg_order_value, favorite_category]
    """
    pass

def weekend_vs_weekday(df):
    """
    Compare weekend vs weekday sales.
    Returns: Dict with weekend and weekday total sales and percentages.
    """
    pass