# Global E-commerce Sales Data Analysis

## 1. Introduction

E-commerce has become an important part of the global retail industry. Businesses generate large amounts of data from customer orders, products, sales, discounts, shipping, and payment methods.

This project analyzes a Global E-commerce Sales dataset to identify important business trends and patterns. The analysis focuses on sales performance, profitability, customer behavior, product performance, geographical performance, and payment methods.

The project uses Python, SQL, Excel, Power Query, and Power BI to perform data cleaning, exploratory data analysis, visualization, and business intelligence.

---

# 2. Project Objectives

The main objectives of this project are:

1. Analyze overall e-commerce sales performance.
2. Calculate total sales and total profit.
3. Identify the highest-performing countries and regions.
4. Analyze product category performance.
5. Identify top-performing products.
6. Analyze customer segments.
7. Identify top customers.
8. Analyze payment methods.
9. Analyze sales trends over time.
10. Identify loss-making products.
11. Analyze the relationship between sales and profit.
12. Build an interactive Power BI dashboard.
13. Generate actionable business insights.

---

# 3. Dataset Description

The dataset contains e-commerce transaction information.

The dataset contains:

- 2,000 records
- 15 original columns

## Original Columns

| Column | Description |
|---|---|
| Order_ID | Unique order identifier |
| Order_Date | Date of order |
| Customer_Name | Customer name |
| Customer_Segment | Customer segment |
| Country | Customer country |
| Region | Geographical region |
| Product_Category | Product category |
| Product_Name | Product name |
| Quantity | Quantity purchased |
| Unit_Price | Price per unit |
| Discount_Percent | Discount percentage |
| Total_Sales | Total sales amount |
| Shipping_Cost | Shipping cost |
| Profit | Profit generated |
| Payment_Method | Payment method |

---

# 4. Tools and Technologies

The following tools were used in this project:

## Python

Libraries:

- Pandas
- NumPy
- Matplotlib
- Seaborn

Python was used for:

- Data loading
- Data cleaning
- Exploratory Data Analysis
- Statistical analysis
- Visualization
- Business insights

## SQL

SQL was used for:

- Aggregation
- Filtering
- Grouping
- Ranking
- Customer analysis
- Product analysis
- Sales analysis

## Microsoft Excel

Excel was used for:

- Power Query
- Data cleaning
- PivotTables
- PivotCharts
- Slicers
- Dashboard creation

## Power BI

Power BI was used for:

- Data modeling
- DAX measures
- Interactive dashboards
- KPI cards
- Charts
- Slicers
- Drill-through
- Business intelligence

---

# 5. Project Workflow

The project follows the following workflow:

Dataset
↓
Data Cleaning
↓
Exploratory Data Analysis
↓
SQL Analysis
↓
Excel Analysis
↓
Power BI Dashboard
↓
Business Insights
↓
Final Recommendations

---

# 6. Data Cleaning

Data cleaning was performed before analysis.

The following steps were performed:

### 6.1 Duplicate Removal

Duplicate records were checked and removed where required.

### 6.2 Missing Value Analysis

Missing values were identified using Pandas.

Numerical missing values were treated using appropriate statistical methods such as median values.

Categorical missing values were treated using the mode where appropriate.

### 6.3 Date Conversion

The `Order_Date` column was converted into a proper date format.

### 6.4 Numerical Data Conversion

The following columns were converted to numeric data types:

- Quantity
- Unit_Price
- Discount_Percent
- Total_Sales
- Shipping_Cost
- Profit

### 6.5 Feature Engineering

Additional columns were created:

- Year
- Month
- Month Name
- Quarter
- Day Name
- Profit Margin
- Gross Sales
- Discount Amount

---

# 7. Key Performance Indicators

The following KPIs were calculated:

## Total Sales

Total revenue generated from all transactions.

Formula:

Total Sales = SUM(Total_Sales)

## Total Profit

Total profit generated from transactions.

Formula:

Total Profit = SUM(Profit)

## Total Orders

Number of unique orders.

Formula:

Total Orders = DISTINCTCOUNT(Order_ID)

## Total Customers

Number of unique customers.

Formula:

Total Customers = DISTINCTCOUNT(Customer_Name)

## Total Products

Number of unique products.

Formula:

Total Products = DISTINCTCOUNT(Product_Name)

## Average Order Value

Formula:

Average Order Value =
Total Sales / Total Orders

## Profit Margin

Formula:

Profit Margin =
Total Profit / Total Sales × 100

---

# 8. Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the dataset and identify important patterns.

---

# 9. Country Analysis

Country-wise sales were analyzed to identify the countries generating the highest revenue.

The analysis includes:

- Total Sales by Country
- Total Profit by Country
- Total Orders by Country
- Quantity Sold by Country

The Top 10 countries were identified using descending sales order.

### Business Question

Which countries contribute the most to total sales?

---

# 10. Regional Analysis

Regional performance was analyzed using:

- Sales
- Profit
- Orders

This helps businesses understand which geographical regions are performing well.

### Business Question

Which region generates the highest sales and profit?

---

# 11. Product Category Analysis

Product categories were analyzed based on:

- Total Sales
- Total Profit
- Quantity Sold
- Number of Orders

This helps identify the most valuable product categories.

### Business Questions

1. Which category has the highest sales?
2. Which category has the highest profit?
3. Which category sells the highest quantity?

---

# 12. Product Analysis

Products were ranked according to sales and profit.

The Top 10 products by sales were identified.

Loss-making products were also analyzed.

### Business Questions

1. Which products generate the highest revenue?
2. Which products generate the highest profit?
3. Which products generate losses?

---

# 13. Customer Analysis

Customer-level analysis was performed to identify high-value customers.

The analysis includes:

- Customer Sales
- Customer Profit
- Number of Orders
- Quantity Purchased

The Top 10 customers were identified based on total sales.

---

# 14. Customer Segment Analysis

Customers were divided into different segments.

Each segment was analyzed using:

- Total Sales
- Total Profit
- Number of Customers
- Number of Orders

### Business Question

Which customer segment contributes the highest revenue?

---

# 15. Payment Method Analysis

Payment methods were analyzed based on:

- Number of orders
- Total sales
- Total profit

This analysis helps understand customer payment preferences.

### Business Question

Which payment method is most commonly used?

---

# 16. Time-Series Analysis

Sales performance was analyzed over time.

The analysis includes:

- Year-wise sales
- Month-wise sales
- Quarter-wise sales

This helps identify:

- Growth trends
- Seasonal patterns
- High-sales periods
- Low-sales periods

---

# 17. Discount Analysis

Discount percentage was analyzed against sales and profit.

The purpose is to understand whether higher discounts have an impact on profitability.

### Business Questions

1. Which discount level generates the highest sales?
2. Which discount level generates the highest profit?
3. Does higher discount reduce profit margin?

---

# 18. Shipping Cost Analysis

Shipping costs were analyzed by country.

The purpose is to identify countries with high shipping expenses.

This can help businesses optimize logistics and shipping strategies.

---

# 19. Sales and Profit Analysis

Sales and profit were compared to identify products or categories that generate high revenue but low profit.

A scatter plot was created to visualize the relationship between:

- Total Sales
- Profit

This helps identify:

- High-sales/high-profit products
- High-sales/low-profit products
- Low-sales/high-profit products
- Loss-making products

---

# 20. Python Visualizations

The following charts were created using Python:

1. Year-wise Sales
2. Monthly Sales Trend
3. Top 10 Countries
4. Sales by Region
5. Sales by Product Category
6. Profit by Product Category
7. Sales by Customer Segment
8. Sales by Payment Method
9. Top 10 Products
10. Top 10 Customers
11. Sales vs Profit
12. Profit Margin Distribution
13. Correlation Heatmap

---

# 21. SQL Analysis

SQL was used to answer important business questions.

Major SQL analyses include:

- Total sales
- Total profit
- Total orders
- Total customers
- Country-wise sales
- Region-wise sales
- Category-wise sales
- Top products
- Top customers
- Customer segment analysis
- Payment method analysis
- Year-wise sales
- Month-wise sales
- Profit margin
- Loss-making products
- Shipping cost analysis
- Top customers by country
- Top products by category

---

# 22. Excel Analysis

Excel was used to create an interactive analysis system.

The Excel project includes:

### Sheets

1. Raw_Data
2. Clean_Data
3. KPI
4. Pivot_Analysis
5. Dashboard

### Excel Features

- Power Query
- PivotTables
- PivotCharts
- Slicers
- Excel formulas
- Dashboard

---

# 23. Power BI Dashboard

A professional Power BI dashboard was created.

## Dashboard Pages

### Page 1 — Executive Dashboard

Includes:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Average Order Value
- Profit Margin
- Monthly Sales Trend
- Sales by Country
- Sales by Category
- Profit by Category
- Customer Segment
- Payment Method

### Page 2 — Product Analysis

Includes:

- Top 10 Products
- Top Profitable Products
- Quantity by Category
- Sales vs Profit

### Page 3 — Customer Analysis

Includes:

- Top Customers
- Customer Segments
- Profit by Segment
- Average Order Value by Segment

### Page 4 — Regional Analysis

Includes:

- Sales by Region
- Profit by Region
- Orders by Region
- Shipping Cost by Country

---

# 24. Power BI DAX Measures

Important DAX measures include:

```DAX
Total Sales =
SUM(SalesData[Total_Sales])