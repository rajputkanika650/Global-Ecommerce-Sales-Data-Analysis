# ============================================================
# GLOBAL E-COMMERCE SALES DATA ANALYSIS
# Complete Python EDA Project
# ============================================================

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# 0. PROJECT PATHS
# ============================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "01_Dataset")

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "02_Python_Analysis",
    "outputs"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

INPUT_FILE = os.path.join(
    DATA_DIR,
    "global_ecommerce_sales.csv"
)

CLEAN_FILE = os.path.join(
    DATA_DIR,
    "clean_global_ecommerce_sales.csv"
)


# ============================================================
# 1. LOAD DATASET
# ============================================================

print("=" * 70)
print("GLOBAL E-COMMERCE SALES DATA ANALYSIS")
print("=" * 70)

print("\nLoading dataset...")

if not os.path.exists(INPUT_FILE):
    print("\nERROR: Dataset file not found!")
    print("Expected file:")
    print(INPUT_FILE)
    raise FileNotFoundError(INPUT_FILE)

df = pd.read_csv(INPUT_FILE)

print("\nDataset loaded successfully!")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])


# ============================================================
# 2. BASIC DATA INFORMATION
# ============================================================

print("\n" + "=" * 70)
print("2. BASIC DATA INFORMATION")
print("=" * 70)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all"))


# ============================================================
# 3. MISSING VALUE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("3. MISSING VALUE ANALYSIS")
print("=" * 70)

missing = df.isnull().sum()

missing_percent = (
    missing / len(df) * 100
)

missing_table = pd.DataFrame({
    "Missing_Values": missing,
    "Missing_Percentage": missing_percent.round(2)
})

print(missing_table)

missing_table.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "missing_values.csv"
    ),
    index=True
)


# ============================================================
# 4. DUPLICATE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("4. DUPLICATE ANALYSIS")
print("=" * 70)

duplicates = df.duplicated().sum()

print("Duplicate rows:", duplicates)

if duplicates > 0:

    df = df.drop_duplicates().copy()

    print("Duplicates removed.")

else:

    print("No duplicate rows found.")


# ============================================================
# 5. DATA TYPE CONVERSION
# ============================================================

print("\n" + "=" * 70)
print("5. DATA TYPE CONVERSION")
print("=" * 70)


# Convert Order Date

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    errors="coerce"
)


# Numerical columns

numeric_columns = [
    "Quantity",
    "Unit_Price",
    "Discount_Percent",
    "Total_Sales",
    "Shipping_Cost",
    "Profit"
]


for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


print("\nOrder_Date converted to datetime.")

print("\nNumerical columns converted.")


# ============================================================
# 6. MISSING VALUE TREATMENT
# ============================================================

print("\n" + "=" * 70)
print("6. MISSING VALUE TREATMENT")
print("=" * 70)


# Numeric columns → Median

for column in numeric_columns:

    if df[column].isnull().sum() > 0:

        median_value = df[column].median()

        df[column] = df[column].fillna(
            median_value
        )


# Categorical columns → Mode

categorical_columns = df.select_dtypes(
    include=["object"]
).columns


for column in categorical_columns:

    if df[column].isnull().sum() > 0:

        mode_value = df[column].mode()

        if not mode_value.empty:

            df[column] = df[column].fillna(
                mode_value.iloc[0]
            )


# Date column → Forward fill

if df["Order_Date"].isnull().sum() > 0:

    df["Order_Date"] = (
        df["Order_Date"]
        .ffill()
        .bfill()
    )


print("Missing values handled.")

print(
    "\nRemaining missing values:"
)

print(
    df.isnull().sum().sum()
)


# ============================================================
# 7. FEATURE ENGINEERING
# ============================================================

print("\n" + "=" * 70)
print("7. FEATURE ENGINEERING")
print("=" * 70)


# Year

df["Year"] = (
    df["Order_Date"]
    .dt.year
)


# Month number

df["Month"] = (
    df["Order_Date"]
    .dt.month
)


# Month name

df["Month_Name"] = (
    df["Order_Date"]
    .dt.month_name()
)


# Quarter

df["Quarter"] = (
    "Q"
    + df["Order_Date"]
    .dt.quarter
    .astype(str)
)


# Day name

df["Day_Name"] = (
    df["Order_Date"]
    .dt.day_name()
)


# ------------------------------------------------------------
# Profit Margin
# ------------------------------------------------------------

df["Profit_Margin"] = np.where(
    df["Total_Sales"] != 0,
    (
        df["Profit"]
        / df["Total_Sales"]
    ) * 100,
    0
)


# ------------------------------------------------------------
# Gross Sales
# ------------------------------------------------------------

df["Gross_Sales"] = np.where(
    df["Discount_Percent"] < 100,
    df["Total_Sales"]
    / (
        1
        - df["Discount_Percent"] / 100
    ),
    df["Total_Sales"]
)


# ------------------------------------------------------------
# Discount Amount
# ------------------------------------------------------------

df["Discount_Amount"] = (
    df["Gross_Sales"]
    - df["Total_Sales"]
)


print("\nCreated columns:")

print("- Year")
print("- Month")
print("- Month_Name")
print("- Quarter")
print("- Day_Name")
print("- Profit_Margin")
print("- Gross_Sales")
print("- Discount_Amount")


# ============================================================
# 8. SAVE CLEAN DATASET
# ============================================================

df.to_csv(
    CLEAN_FILE,
    index=False
)

print("\nClean dataset saved successfully!")

print(CLEAN_FILE)


# ============================================================
# 9. KEY PERFORMANCE INDICATORS
# ============================================================

print("\n" + "=" * 70)
print("9. KEY PERFORMANCE INDICATORS")
print("=" * 70)


total_sales = df["Total_Sales"].sum()

total_profit = df["Profit"].sum()

total_quantity = df["Quantity"].sum()

total_orders = df["Order_ID"].nunique()

total_customers = df["Customer_Name"].nunique()

total_products = df["Product_Name"].nunique()


if total_orders > 0:

    average_order_value = (
        total_sales / total_orders
    )

else:

    average_order_value = 0


if total_sales != 0:

    overall_profit_margin = (
        total_profit
        / total_sales
        * 100
    )

else:

    overall_profit_margin = 0


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

        overall_profit_margin

    ]

})


print("\nKPI Summary:")

print(
    kpi.to_string(index=False)
)


kpi.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "kpi_summary.csv"
    ),
    index=False
)


# ============================================================
# 10. COUNTRY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("10. COUNTRY-WISE ANALYSIS")
print("=" * 70)


country_analysis = (

    df.groupby(
        "Country",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        ),

        Quantity=(
            "Quantity",
            "sum"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print("\nTop 10 Countries:")

print(
    country_analysis.head(10)
)


country_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "country_analysis.csv"
    ),
    index=False
)


# ============================================================
# 11. REGION ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("11. REGION-WISE ANALYSIS")
print("=" * 70)


region_analysis = (

    df.groupby(
        "Region",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print(region_analysis)


region_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "region_analysis.csv"
    ),
    index=False
)


# ============================================================
# 12. PRODUCT CATEGORY ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("12. PRODUCT CATEGORY ANALYSIS")
print("=" * 70)


category_analysis = (

    df.groupby(
        "Product_Category",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Quantity=(
            "Quantity",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print(category_analysis)


category_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "category_analysis.csv"
    ),
    index=False
)


# ============================================================
# 13. PRODUCT ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("13. PRODUCT ANALYSIS")
print("=" * 70)


product_analysis = (

    df.groupby(
        "Product_Name",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Quantity=(
            "Quantity",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print("\nTop 10 Products:")

print(
    product_analysis.head(10)
)


print("\nBottom 10 Products:")

print(
    product_analysis.tail(10)
)


product_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "product_analysis.csv"
    ),
    index=False
)


# ============================================================
# 14. CUSTOMER ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("14. CUSTOMER ANALYSIS")
print("=" * 70)


customer_analysis = (

    df.groupby(
        "Customer_Name",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        ),

        Quantity=(
            "Quantity",
            "sum"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print("\nTop 10 Customers:")

print(
    customer_analysis.head(10)
)


customer_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "customer_analysis.csv"
    ),
    index=False
)


# ============================================================
# 15. CUSTOMER SEGMENT ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("15. CUSTOMER SEGMENT ANALYSIS")
print("=" * 70)


segment_analysis = (

    df.groupby(
        "Customer_Segment",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        ),

        Customers=(
            "Customer_Name",
            "nunique"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print(segment_analysis)


segment_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "customer_segment_analysis.csv"
    ),
    index=False
)


# ============================================================
# 16. PAYMENT METHOD ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("16. PAYMENT METHOD ANALYSIS")
print("=" * 70)


payment_analysis = (

    df.groupby(
        "Payment_Method",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        ),

        Profit=(
            "Profit",
            "sum"
        )

    )

    .sort_values(
        "Sales",
        ascending=False
    )

)


print(payment_analysis)


payment_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "payment_method_analysis.csv"
    ),
    index=False
)


# ============================================================
# 17. YEAR-WISE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("17. YEAR-WISE ANALYSIS")
print("=" * 70)


year_analysis = (

    df.groupby(
        "Year",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        ),

        Quantity=(
            "Quantity",
            "sum"
        )

    )

    .sort_values("Year")

)


print(year_analysis)


year_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "year_analysis.csv"
    ),
    index=False
)


# ============================================================
# 18. MONTH-WISE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("18. MONTH-WISE ANALYSIS")
print("=" * 70)


month_analysis = (

    df.groupby(
        "Month",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

    .sort_values("Month")

)


print(month_analysis)


month_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "month_analysis.csv"
    ),
    index=False
)


# ============================================================
# 19. QUARTER-WISE ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("19. QUARTER-WISE ANALYSIS")
print("=" * 70)


quarter_analysis = (

    df.groupby(
        "Quarter",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

)


quarter_order = [
    "Q1",
    "Q2",
    "Q3",
    "Q4"
]


quarter_analysis["Quarter"] = pd.Categorical(
    quarter_analysis["Quarter"],
    categories=quarter_order,
    ordered=True
)


quarter_analysis = (
    quarter_analysis
    .sort_values("Quarter")
)


print(quarter_analysis)


quarter_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "quarter_analysis.csv"
    ),
    index=False
)


# ============================================================
# 20. LOSS-MAKING PRODUCTS
# ============================================================

print("\n" + "=" * 70)
print("20. LOSS-MAKING PRODUCTS")
print("=" * 70)


loss_products = (

    product_analysis[
        product_analysis["Profit"] < 0
    ]

    .sort_values(
        "Profit",
        ascending=True
    )

)


print(
    loss_products.head(10)
)


loss_products.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "loss_making_products.csv"
    ),
    index=False
)


# ============================================================
# 21. TOP PROFITABLE PRODUCTS
# ============================================================

print("\n" + "=" * 70)
print("21. TOP PROFITABLE PRODUCTS")
print("=" * 70)


top_profit_products = (

    product_analysis

    .sort_values(
        "Profit",
        ascending=False
    )

    .head(10)

)


print(top_profit_products)


top_profit_products.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "top_profitable_products.csv"
    ),
    index=False
)


# ============================================================
# 22. DISCOUNT ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("22. DISCOUNT ANALYSIS")
print("=" * 70)


discount_analysis = (

    df.groupby(
        "Discount_Percent",
        as_index=False
    )

    .agg(

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Profit=(
            "Profit",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

    .sort_values(
        "Discount_Percent"
    )

)


print(discount_analysis)


discount_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "discount_analysis.csv"
    ),
    index=False
)


# ============================================================
# 23. SHIPPING COST ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("23. SHIPPING COST ANALYSIS")
print("=" * 70)


shipping_analysis = (

    df.groupby(
        "Country",
        as_index=False
    )

    .agg(

        Shipping_Cost=(
            "Shipping_Cost",
            "sum"
        ),

        Sales=(
            "Total_Sales",
            "sum"
        ),

        Orders=(
            "Order_ID",
            "nunique"
        )

    )

    .sort_values(
        "Shipping_Cost",
        ascending=False
    )

)


print(
    shipping_analysis.head(10)
)


shipping_analysis.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "shipping_analysis.csv"
    ),
    index=False
)


# ============================================================
# 24. VISUALIZATION SETUP
# ============================================================

print("\n" + "=" * 70)
print("24. CREATING VISUALIZATIONS")
print("=" * 70)


sns.set_theme(
    style="whitegrid"
)


# ============================================================
# CHART 1 - YEARLY SALES
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    data=year_analysis,
    x="Year",
    y="Sales"
)

plt.title(
    "Year-wise Sales"
)

plt.xlabel("Year")

plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "01_yearly_sales.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 2 - MONTHLY SALES
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.lineplot(
    data=month_analysis,
    x="Month",
    y="Sales",
    marker="o"
)

plt.title(
    "Monthly Sales Trend"
)

plt.xlabel("Month")

plt.ylabel("Total Sales")

plt.xticks(
    range(1, 13)
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "02_monthly_sales.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 3 - TOP COUNTRIES
# ============================================================

top_countries = (
    country_analysis
    .head(10)
)


plt.figure(
    figsize=(12, 7)
)

sns.barplot(
    data=top_countries,
    x="Sales",
    y="Country"
)

plt.title(
    "Top 10 Countries by Sales"
)

plt.xlabel("Total Sales")

plt.ylabel("Country")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "03_top_countries.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 4 - REGION SALES
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    data=region_analysis,
    x="Region",
    y="Sales"
)

plt.title(
    "Sales by Region"
)

plt.xlabel("Region")

plt.ylabel("Total Sales")

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "04_region_sales.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 5 - CATEGORY SALES
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    data=category_analysis,
    x="Product_Category",
    y="Sales"
)

plt.title(
    "Sales by Product Category"
)

plt.xlabel(
    "Product Category"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "05_category_sales.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 6 - CATEGORY PROFIT
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    data=category_analysis,
    x="Product_Category",
    y="Profit"
)

plt.title(
    "Profit by Product Category"
)

plt.xlabel(
    "Product Category"
)

plt.ylabel(
    "Profit"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "06_category_profit.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 7 - CUSTOMER SEGMENT
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    data=segment_analysis,
    x="Customer_Segment",
    y="Sales"
)

plt.title(
    "Sales by Customer Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Sales"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "07_customer_segment.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 8 - PAYMENT METHOD
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.barplot(
    data=payment_analysis,
    x="Payment_Method",
    y="Sales"
)

plt.title(
    "Sales by Payment Method"
)

plt.xlabel(
    "Payment Method"
)

plt.ylabel(
    "Sales"
)

plt.xticks(
    rotation=30
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "08_payment_method.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 9 - TOP PRODUCTS
# ============================================================

top_products = (
    product_analysis
    .head(10)
)


plt.figure(
    figsize=(12, 7)
)

sns.barplot(
    data=top_products,
    x="Sales",
    y="Product_Name"
)

plt.title(
    "Top 10 Products by Sales"
)

plt.xlabel("Sales")

plt.ylabel("Product")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "09_top_products.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 10 - TOP CUSTOMERS
# ============================================================

top_customers = (
    customer_analysis
    .head(10)
)


plt.figure(
    figsize=(12, 7)
)

sns.barplot(
    data=top_customers,
    x="Sales",
    y="Customer_Name"
)

plt.title(
    "Top 10 Customers by Sales"
)

plt.xlabel("Sales")

plt.ylabel("Customer")

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "10_top_customers.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 11 - SALES VS PROFIT
# ============================================================

plt.figure(
    figsize=(10, 7)
)

sns.scatterplot(
    data=df,
    x="Total_Sales",
    y="Profit",
    hue="Product_Category",
    s=70
)

plt.title(
    "Sales vs Profit"
)

plt.xlabel(
    "Total Sales"
)

plt.ylabel(
    "Profit"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "11_sales_vs_profit.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# CHART 12 - PROFIT MARGIN DISTRIBUTION
# ============================================================

plt.figure(
    figsize=(10, 6)
)

sns.histplot(
    df["Profit_Margin"],
    bins=30,
    kde=True
)

plt.title(
    "Profit Margin Distribution"
)

plt.xlabel(
    "Profit Margin (%)"
)

plt.ylabel(
    "Frequency"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "12_profit_margin_distribution.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 25. CORRELATION ANALYSIS
# ============================================================

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


correlation_matrix = (
    df[correlation_columns]
    .corr()
)


print(
    correlation_matrix
)


correlation_matrix.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "correlation_matrix.csv"
    )
)


# ============================================================
# CHART 13 - CORRELATION HEATMAP
# ============================================================

plt.figure(
    figsize=(10, 7)
)

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title(
    "Correlation Matrix"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        OUTPUT_DIR,
        "13_correlation_heatmap.png"
    ),
    dpi=300
)

plt.close()


# ============================================================
# 26. FINAL BUSINESS INSIGHTS
# ============================================================

print("\n" + "=" * 70)
print("26. FINAL BUSINESS INSIGHTS")
print("=" * 70)


# Best country

best_country_row = (
    country_analysis
    .iloc[0]
)

best_country = (
    best_country_row["Country"]
)

best_country_sales = (
    best_country_row["Sales"]
)


# Best category

best_category_row = (
    category_analysis
    .iloc[0]
)

best_category = (
    best_category_row["Product_Category"]
)

best_category_sales = (
    best_category_row["Sales"]
)


# Best customer segment

best_segment_row = (
    segment_analysis
    .iloc[0]
)

best_segment = (
    best_segment_row["Customer_Segment"]
)

best_segment_sales = (
    best_segment_row["Sales"]
)


# Best payment method

best_payment = (
    payment_analysis
    .iloc[0]["Payment_Method"]
)


# Best product

best_product_row = (
    product_analysis
    .iloc[0]
)

best_product = (
    best_product_row["Product_Name"]
)

best_product_sales = (
    best_product_row["Sales"]
)


print(
    f"\n1. Highest Sales Country: "
    f"{best_country}"
)

print(
    f"   Sales: "
    f"{best_country_sales:,.2f}"
)


print(
    f"\n2. Best Product Category: "
    f"{best_category}"
)

print(
    f"   Sales: "
    f"{best_category_sales:,.2f}"
)


print(
    f"\n3. Best Customer Segment: "
    f"{best_segment}"
)

print(
    f"   Sales: "
    f"{best_segment_sales:,.2f}"
)


print(
    f"\n4. Best Payment Method: "
    f"{best_payment}"
)


print(
    f"\n5. Best Product by Sales: "
    f"{best_product}"
)

print(
    f"   Sales: "
    f"{best_product_sales:,.2f}"
)


print(
    f"\n6. Total Sales: "
    f"{total_sales:,.2f}"
)


print(
    f"7. Total Profit: "
    f"{total_profit:,.2f}"
)


print(
    f"8. Overall Profit Margin: "
    f"{overall_profit_margin:.2f}%"
)


print(
    f"9. Total Orders: "
    f"{total_orders:,}"
)


print(
    f"10. Total Customers: "
    f"{total_customers:,}"
)


print(
    f"11. Total Products: "
    f"{total_products:,}"
)


# ============================================================
# 27. FINAL BUSINESS SUMMARY
# ============================================================

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

        "Total Customers",

        "Total Products"

    ],

    "Value": [

        best_country,

        best_category,

        best_segment,

        best_payment,

        best_product,

        total_sales,

        total_profit,

        overall_profit_margin,

        total_orders,

        total_customers,

        total_products

    ]

})


summary.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "final_business_summary.csv"
    ),
    index=False
)


# ============================================================
# 28. SAVE DATASET OVERVIEW
# ============================================================

dataset_overview = pd.DataFrame({

    "Metric": [

        "Rows",

        "Columns",

        "Duplicate Rows Removed",

        "Missing Values Remaining",

        "Total Sales",

        "Total Profit",

        "Total Orders",

        "Total Customers",

        "Total Products"

    ],

    "Value": [

        len(df),

        len(df.columns),

        duplicates,

        int(df.isnull().sum().sum()),

        total_sales,

        total_profit,

        total_orders,

        total_customers,

        total_products

    ]

})


dataset_overview.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "dataset_overview.csv"
    ),
    index=False
)


# ============================================================
# PROJECT COMPLETED
# ============================================================

print("\n" + "=" * 70)
print("PROJECT ANALYSIS COMPLETED SUCCESSFULLY!")
print("=" * 70)

print("\nResults saved in:")

print(OUTPUT_DIR)

print("\nGenerated files include:")

print("- clean_global_ecommerce_sales.csv")

print("- kpi_summary.csv")

print("- missing_values.csv")

print("- country_analysis.csv")

print("- region_analysis.csv")

print("- category_analysis.csv")

print("- product_analysis.csv")

print("- customer_analysis.csv")

print("- customer_segment_analysis.csv")

print("- payment_method_analysis.csv")

print("- year_analysis.csv")

print("- month_analysis.csv")

print("- quarter_analysis.csv")

print("- loss_making_products.csv")

print("- top_profitable_products.csv")

print("- discount_analysis.csv")

print("- shipping_analysis.csv")

print("- correlation_matrix.csv")

print("- final_business_summary.csv")

print("- 13 PNG charts")

print("\nDone!")