global_ecommerce_sales.csv
Spreadsheet
ye h dataset ab project folder do

Haan 👍 Tumhara Global E-commerce Sales dataset check kar liya hai — 2,000 rows × 15 columns hain.

Maine tumhare liye proper Data Analyst project folder structure bana diya hai:

Global_Ecommerce_Sales_Data_Analysis_Project
│
├── 01_Dataset
│   └── global_ecommerce_sales.csv
│
├── 02_Python_Analysis
│   ├── analysis_starter.py
│   └── dataset_overview.csv
│
├── 03_SQL_Analysis
│   └── analysis_queries.sql
│
├── 04_Excel_Analysis
│   └── excel_project_plan.txt
│
├── 05_PowerBI
│   └── powerbi_dashboard_plan.txt
│
├── 06_Reports
│   └── project_report.md
│
├── 07_Kaggle
│   └── kaggle_project_description.md
│
└── README.md
Dataset ke columns

Order_ID, Order_Date, Customer_Name, Customer_Segment, Country, Region, Product_Category, Product_Name, Quantity, Unit_Price, Discount_Percent, Total_Sales, Shipping_Cost, Profit, Payment_Method

📦 Complete Project Folder

Download Global E-commerce Data Analysis Project ZIP

Next step: main isi dataset par tumhare liye 
complete project step-by-step bana sakta hoon — Python EDA + 20 business questions + SQL queries + Excel dashboard + Power BI dashboard + final insights + Kaggle upload-ready files. 

is folder se hisab se one by one code do

Bilkul. Hum folder ke exact order me one-by-one project banayenge. Abhi Step 1: 01_Dataset + 02_Python_Analysis se start karte hain.

Step 1 — Dataset Load & Basic Analysis

Tumhari file:

01_Dataset/global_ecommerce_sales.csv

Python file:

02_Python_Analysis/analysis_starter.py

Is code ko analysis_starter.py me paste karo:

# ==========================================




# ------------------------------------------
# 11. Unique Values
# ------------------------------------------


print("\nUnique Values in Important Columns:")


print("\nCountries:")
print(df["Country"].unique())


print("\nCustomer Segments:")
print(df["Customer_Segment"].unique())


print("\nProduct Categories:")
print(df["Product_Category"].unique())


print("\nPayment Methods:")
print(df["Payment_Method"].unique())




# ------------------------------------------
# 12. Number of Unique Values
# ------------------------------------------


print("\nNumber of Unique Values:")


print("Countries:",
      df["Country"].nunique())


print("Customers:",
      df["Customer_Name"].nunique())


print("Products:",
      df["Product_Name"].nunique())


print("Categories:",
      df["Product_Category"].nunique())




# ------------------------------------------
# 13. Total Sales
# ------------------------------------------


total_sales = df["Total_Sales"].sum()


print("\nTotal Sales:")
print(total_sales)




# ------------------------------------------
# 14. Total Profit
# ------------------------------------------


total_profit = df["Profit"].sum()


print("\nTotal Profit:")
print(total_profit)




# ------------------------------------------
# 15. Total Quantity Sold
# ------------------------------------------


total_quantity = df["Quantity"].sum()


print("\nTotal Quantity Sold:")
print(total_quantity)




# ------------------------------------------
# 16. Average Order Value
# ------------------------------------------


average_order_value = df["Total_Sales"].mean()


print("\nAverage Order Value:")
print(average_order_value)




print("\n" + "=" * 50)
print("STEP 1 COMPLETED")
print("=" * 50)
Run karne ke baad

Tumhe roughly ye information milegi:

Dataset me 2000 rows
15 columns
Total Sales
Total Profit
Total Quantity
Average Sales
Countries
Customers
Products
Categories
Payment Methods
Missing values
Duplicate rows
Step 2 — Data Cleaning

Ab isi file me next section add karna hai:

# ==========================================
print("\nNumerical Columns:")
print(numeric_columns)




# ------------------------------------------
# 7. Create Profit Margin Column
# ------------------------------------------


df["Profit_Margin"] = (
    df["Profit"] / df["Total_Sales"]
) * 100


print("\nProfit Margin Created.")




# ------------------------------------------
# 8. Create Year Column
# ------------------------------------------


df["Year"] = df["Order_Date"].dt.year


print("\nYear Column Created.")




# ------------------------------------------
# 9. Create Month Column
# ------------------------------------------


df["Month"] = df["Order_Date"].dt.month


print("\nMonth Column Created.")




# ------------------------------------------
# 10. Create Month Name
# ------------------------------------------


df["Month_Name"] = df["Order_Date"].dt.month_name()


print("\nMonth Name Column Created.")




# ------------------------------------------
# 11. Create Quarter Column
# ------------------------------------------


df["Quarter"] = df["Order_Date"].dt.quarter


print("\nQuarter Column Created.")




# ------------------------------------------
# 12. Final Dataset Information
# ------------------------------------------


print("\nFinal Dataset Shape:")
print(df.shape)




# ------------------------------------------
# 13. Save Clean Dataset
# ------------------------------------------


df.to_csv(
    "../01_Dataset/clean_global_ecommerce_sales.csv",
    index=False
)


print("\nClean dataset saved successfully!")


print("\n" + "=" * 50)
print("STEP 2 COMPLETED")
print("=" * 50)
Is step ke baad

Tumhare 01_Dataset folder me ek new file ban jayegi:

01_Dataset
│
├── global_ecommerce_sales.csv
└── clean_global_ecommerce_sales.csv

Aur clean dataset me naye columns honge:

Profit_Margin
Year
Month
Month_Name
Quarter
Step 3 — Exploratory Data Analysis

Iske baad hum actual analysis start karenge:

📈 Year-wise Sales
📅 Month-wise Sales
🌍 Country-wise Sales
🗺️ Region-wise Sales
📦 Category-wise Sales
🏆 Top 10 Products
👤 Customer Segment Analysis
💰 Profit Analysis
💳 Payment Method Analysis
📊 Sales vs Profit
🔥 Top 10 Customers
📉 Loss-making Products
📈 Sales Trend Charts

Next hum Step 3 ka complete Python EDA code banayenge, jo isi dataset ke columns ke according hoga.

full code do
Analyzed

Bilkul 👍 Maine tumhare Global E-commerce Sales dataset ke according complete Python analysis code bana diya hai.

📥 Full Python Code

Download full_analysis.py

Ye code automatically:

Dataset load karega
Data information check karega
Missing values analyze karega
Duplicate rows remove karega
Date & numerical columns clean karega
New columns create karega:
Year
Month
Quarter
Day Name
Profit Margin
Gross Sales
Discount Amount
Total Sales calculate karega
Total Profit calculate karega
Total Orders/Customers/Products nikalega
Country analysis
Region analysis
Product Category analysis
Product analysis
Customer analysis
Customer Segment analysis
Payment Method analysis
Year-wise analysis
Month-wise analysis
Quarter-wise analysis
Loss-making products
Top profitable products
Discount analysis
Shipping cost analysis
12+ charts generate karega
Correlation analysis karega
Final business insights generate karega
Saare results 02_Python_Analysis/outputs/ me save karega
▶️ Run karne ka tarika

Terminal me project folder ke andar:

pip install pandas numpy matplotlib seaborn

Phir:

python 02_Python_Analysis/full_analysis.py

Important: File ko project folder ke structure ke according hi rakho, taaki relative paths properly work karein.

Uske baad next folder 03_SQL_Analysis par jayenge aur isi dataset ke liye complete SQL code (20+ queries) banayenge. 

full_analysis.py
Code

Library
/
full_analysis.py
# ============================================================
# GLOBAL E-COMMERCE SALES DATA ANALYSIS
# Complete Python Project
# ============================================================
# Author: Data Analyst Portfolio Project
# Dataset: global_ecommerce_sales.csv
#
# Libraries required:
# pandas, numpy, matplotlib, seaborn
#
# Install if required:
# pip install pandas numpy matplotlib seaborn
# ============================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 0. Project Paths
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "01_Dataset")
OUTPUT_DIR = os.path.join(BASE_DIR, "02_Python_Analysis", "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

INPUT_FILE = os.path.join(DATA_DIR, "global_ecommerce_sales.csv")
CLEAN_FILE = os.path.join(DATA_DIR, "clean_global_ecommerce_sales.csv")

# ------------------------------------------------------------
# 1. Load Dataset
# ------------------------------------------------------------

print("=" * 70)
print("GLOBAL E-COMMERCE SALES DATA ANALYSIS")
print("=" * 70)

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# ------------------------------------------------------------
# 2. Basic Dataset Information
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("2. BASIC DATA INFORMATION")
print("=" * 70)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all"))

# ------------------------------------------------------------
# 3. Missing Values
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("3. MISSING VALUE ANALYSIS")
print("=" * 70)

missing = df.isnull().sum()
missing_percent = (missing / len(df)) * 100

missing_table = pd.DataFrame({
    "Missing_Values": missing,
    "Missing_Percentage": missing_percent.round(2)
})

print(missing_table)

missing_table.to_csv(
    os.path.join(OUTPUT_DIR, "missing_values.csv")
)

# ------------------------------------------------------------
# 4. Duplicate Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("4. DUPLICATE ANALYSIS")
print("=" * 70)

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates().copy()
    print("Duplicates removed.")

# ------------------------------------------------------------
# 5. Data Type Conversion
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("5. DATA TYPE CONVERSION")
print("=" * 70)

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Total_Sales",
    "Shipping_Cost",
    "Profit"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("Order_Date converted to datetime.")

# ------------------------------------------------------------
# 6. Missing Value Treatment
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("6. MISSING VALUE TREATMENT")
print("=" * 70)

# Numeric columns: median
for col in numeric_columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

# Text columns: mode
categorical_columns = df.select_dtypes(
    include=["object"]
).columns

for col in categorical_columns:
    if df[col].isnull().sum() > 0:
        mode_value = df[col].mode()
        if not mode_value.empty:
            df[col] = df[col].fillna(mode_value.iloc[0])

print("Missing values handled.")

# ------------------------------------------------------------
# 7. Feature Engineering
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("7. FEATURE ENGINEERING")
print("=" * 70)

df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.month_name()
df["Quarter"] = "Q" + df["Order_Date"].dt.quarter.astype(str)
df["Day_Name"] = df["Order_Date"].dt.day_name()

# Profit margin
df["Profit_Margin"] = np.where(
    df["Total_Sales"] != 0,
    (df["Profit"] / df["Total_Sales"]) * 100,
    0
)

# Revenue before discount estimate
df["Gross_Sales"] = np.where(
    df["Discount_Percent"] < 100,
    df["Total_Sales"] / (1 - df["Discount_Percent"] / 100),
    df["Total_Sales"]
)

# Discount amount estimate
df["Discount_Amount"] = (
    df["Gross_Sales"] - df["Total_Sales"]
)

print("Created:")
print("- Year")
print("- Month")
print("- Month_Name")
print("- Quarter")
print("- Day_Name")
print("- Profit_Margin")
print("- Gross_Sales")
print("- Discount_Amount")

# ------------------------------------------------------------
# 8. Save Clean Dataset
# ------------------------------------------------------------

df.to_csv(CLEAN_FILE, index=False)

print("\nClean dataset saved:")
print(CLEAN_FILE)

# ------------------------------------------------------------
# 9. KPI ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("9. KEY PERFORMANCE INDICATORS")
print("=" * 70)

total_sales = df["Total_Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_Name"].nunique()
total_products = df["Product_Name"].nunique()
average_order_value = df["Total_Sales"].sum() / total_orders
profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

kpi = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Profit",
        "Total Quantity",
        "Total Orders",
        "Total Customers",
        "Total Products",
        "Average Order Value",
        "Overall Profit Margin"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_quantity,
        total_orders,
        total_customers,
        total_products,
        average_order_value,
        profit_margin
    ]
})

print(kpi.to_string(index=False))

kpi.to_csv(
    os.path.join(OUTPUT_DIR, "kpi_summary.csv"),
    index=False
)

# ------------------------------------------------------------
# 10. Country Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("10. COUNTRY-WISE ANALYSIS")
print("=" * 70)

country_sales = (
    df.groupby("Country", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\nTop Countries by Sales:")
print(country_sales.head(10))

country_sales.to_csv(
    os.path.join(OUTPUT_DIR, "country_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 11. Region Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("11. REGION-WISE ANALYSIS")
print("=" * 70)

region_sales = (
    df.groupby("Region", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique")
      )
      .sort_values("Sales", ascending=False)
)

print(region_sales)

region_sales.to_csv(
    os.path.join(OUTPUT_DIR, "region_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 12. Product Category Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("12. PRODUCT CATEGORY ANALYSIS")
print("=" * 70)

category_analysis = (
    df.groupby("Product_Category", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum"),
          Orders=("Order_ID", "nunique")
      )
      .sort_values("Sales", ascending=False)
)

print(category_analysis)

category_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "category_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 13. Product Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("13. PRODUCT ANALYSIS")
print("=" * 70)

product_analysis = (
    df.groupby("Product_Name", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum"),
          Orders=("Order_ID", "nunique")
      )
      .sort_values("Sales", ascending=False)
)

print("\nTop 10 Products:")
print(product_analysis.head(10))

print("\nBottom 10 Products:")
print(product_analysis.tail(10))

product_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "product_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 14. Customer Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("14. CUSTOMER ANALYSIS")
print("=" * 70)

customer_analysis = (
    df.groupby("Customer_Name", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\nTop 10 Customers:")
print(customer_analysis.head(10))

customer_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "customer_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 15. Customer Segment Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("15. CUSTOMER SEGMENT ANALYSIS")
print("=" * 70)

segment_analysis = (
    df.groupby("Customer_Segment", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique"),
          Customers=("Customer_Name", "nunique")
      )
      .sort_values("Sales", ascending=False)
)

print(segment_analysis)

segment_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "customer_segment_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 16. Payment Method Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("16. PAYMENT METHOD ANALYSIS")
print("=" * 70)

payment_analysis = (
    df.groupby("Payment_Method", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Orders=("Order_ID", "nunique"),
          Profit=("Profit", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print(payment_analysis)

payment_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "payment_method_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 17. Year-wise Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("17. YEAR-WISE ANALYSIS")
print("=" * 70)

year_analysis = (
    df.groupby("Year", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Year")
)

print(year_analysis)

year_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "year_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 18. Month-wise Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("18. MONTH-WISE ANALYSIS")
print("=" * 70)

month_analysis = (
    df.groupby("Month", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique")
      )
      .sort_values("Month")
)

print(month_analysis)

month_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "month_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 19. Quarter Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("19. QUARTER-WISE ANALYSIS")
print("=" * 70)

quarter_analysis = (
    df.groupby("Quarter", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique")
      )
)

quarter_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "quarter_analysis.csv"),
    index=False
)

print(quarter_analysis)

# ------------------------------------------------------------
# 20. Loss-Making Products
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("20. LOSS-MAKING PRODUCTS")
print("=" * 70)

loss_products = (
    product_analysis[
        product_analysis["Profit"] < 0
    ]
    .sort_values("Profit")
)

print(loss_products.head(10))

loss_products.to_csv(
    os.path.join(OUTPUT_DIR, "loss_making_products.csv"),
    index=False
)

# ------------------------------------------------------------
# 21. Top Profitable Products
# ------------------------------------------------------------

top_profit_products = (
    product_analysis
    .sort_values("Profit", ascending=False)
    .head(10)
)

print("\nTop 10 Profitable Products:")
print(top_profit_products)

top_profit_products.to_csv(
    os.path.join(OUTPUT_DIR, "top_profitable_products.csv"),
    index=False
)

# ------------------------------------------------------------
# 22. Discount Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("22. DISCOUNT ANALYSIS")
print("=" * 70)

discount_analysis = (
    df.groupby("Discount_Percent", as_index=False)
      .agg(
          Sales=("Total_Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "nunique")
      )
      .sort_values("Discount_Percent")
)

print(discount_analysis)

discount_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "discount_analysis.csv"),
    index=False
)

# ------------------------------------------------------------
# 23. Shipping Cost Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("23. SHIPPING COST ANALYSIS")
print("=" * 70)

shipping_analysis = (
    df.groupby("Country", as_index=False)
      .agg(
          Shipping_Cost=("Shipping_Cost", "sum"),
          Sales=("Total_Sales", "sum"),
          Orders=("Order_ID", "nunique")
      )
      .sort_values("Shipping_Cost", ascending=False)
)

print(shipping_analysis.head(10))

shipping_analysis.to_csv(
    os.path.join(OUTPUT_DIR, "shipping_analysis.csv"),
    index=False
)

# ============================================================
# 24. VISUALIZATION SECTION
# ============================================================

sns.set_theme(style="whitegrid")

# ------------------------------------------------------------
# Chart 1: Yearly Sales
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=year_analysis,
    x="Year",
    y="Sales"
)

plt.title("Year-wise Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "01_yearly_sales.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 2: Monthly Sales
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.lineplot(
    data=month_analysis,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(range(1, 13))
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "02_monthly_sales.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 3: Sales by Country
# ------------------------------------------------------------

top_countries = country_sales.head(10)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_countries,
    x="Sales",
    y="Country"
)

plt.title("Top 10 Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "03_top_countries.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 4: Sales by Region
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=region_sales,
    x="Region",
    y="Sales"
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "04_region_sales.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 5: Category Sales
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_analysis,
    x="Product_Category",
    y="Sales"
)

plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "05_category_sales.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 6: Category Profit
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=category_analysis,
    x="Product_Category",
    y="Profit"
)

plt.title("Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Profit")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "06_category_profit.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 7: Customer Segment
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=segment_analysis,
    x="Customer_Segment",
    y="Sales"
)

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "07_customer_segment.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 8: Payment Method
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.barplot(
    data=payment_analysis,
    x="Payment_Method",
    y="Sales"
)

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Sales")
plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "08_payment_method.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 9: Top 10 Products
# ------------------------------------------------------------

top_products = product_analysis.head(10)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_products,
    x="Sales",
    y="Product_Name"
)

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "09_top_products.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 10: Top 10 Customers
# ------------------------------------------------------------

top_customers = customer_analysis.head(10)

plt.figure(figsize=(12, 7))

sns.barplot(
    data=top_customers,
    x="Sales",
    y="Customer_Name"
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales")
plt.ylabel("Customer")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "10_top_customers.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 11: Sales vs Profit
# ------------------------------------------------------------

plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df,
    x="Total_Sales",
    y="Profit",
    hue="Product_Category",
    s=70
)

plt.title("Sales vs Profit")
plt.xlabel("Total Sales")
plt.ylabel("Profit")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "11_sales_vs_profit.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# Chart 12: Profit Margin Distribution
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    df["Profit_Margin"],
    bins=30,
    kde=True
)

plt.title("Profit Margin Distribution")
plt.xlabel("Profit Margin (%)")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "12_profit_margin_distribution.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# 25. Correlation Analysis
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("25. CORRELATION ANALYSIS")
print("=" * 70)

correlation_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Total_Sales",
    "Shipping_Cost",
    "Profit",
    "Profit_Margin"
]

correlation_matrix = df[
    correlation_columns
].corr()

print(correlation_matrix)

correlation_matrix.to_csv(
    os.path.join(OUTPUT_DIR, "correlation_matrix.csv")
)

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Matrix")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "13_correlation_heatmap.png"),
    dpi=300
)

plt.show()

# ------------------------------------------------------------
# 26. Final Business Insights
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("26. FINAL BUSINESS INSIGHTS")
print("=" * 70)

best_country = country_sales.iloc[0]["Country"]
best_country_sales = country_sales.iloc[0]["Sales"]

best_category = category_analysis.iloc[0]["Product_Category"]
best_category_sales = category_analysis.iloc[0]["Sales"]

best_segment = segment_analysis.iloc[0]["Customer_Segment"]
best_segment_sales = segment_analysis.iloc[0]["Sales"]

best_payment = payment_analysis.iloc[0]["Payment_Method"]

best_product = product_analysis.iloc[0]["Product_Name"]
best_product_sales = product_analysis.iloc[0]["Sales"]

print(f"\n1. Highest Sales Country: {best_country}")
print(f"   Sales: {best_country_sales:,.2f}")

print(f"\n2. Best Product Category: {best_category}")
print(f"   Sales: {best_category_sales:,.2f}")

print(f"\n3. Best Customer Segment: {best_segment}")
print(f"   Sales: {best_segment_sales:,.2f}")

print(f"\n4. Most Used/Highest Sales Payment Method: {best_payment}")

print(f"\n5. Best Product by Sales: {best_product}")
print(f"   Sales: {best_product_sales:,.2f}")

print(f"\n6. Total Sales: {total_sales:,.2f}")
print(f"7. Total Profit: {total_profit:,.2f}")
print(f"8. Overall Profit Margin: {profit_margin:.2f}%")
print(f"9. Total Orders: {total_orders:,}")
print(f"10. Total Customers: {total_customers:,}")

# ------------------------------------------------------------
# 27. Save Final Summary
# ------------------------------------------------------------

summary = pd.DataFrame({
    "Metric": [
        "Highest Sales Country",
        "Best Product Category",
        "Best Customer Segment",
        "Best Payment Method",
        "Best Product",
        "Total Sales",
        "Total Profit",
        "Profit Margin",
        "Total Orders",
        "Total Customers"
    ],
    "Value": [
        best_country,
        best_category,
        best_segment,
        best_payment,
        best_product,
        total_sales,
        total_profit,
        profit_margin,
        total_orders,
        total_customers
    ]
})

summary.to_csv(
    os.path.join(OUTPUT_DIR, "final_business_summary.csv"),
    index=False
)

print("\nFinal summary saved.")

print("\n" + "=" * 70)
print("PROJECT ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 70)
print("\nCheck the folder:")
print(OUTPUT_DIR)
