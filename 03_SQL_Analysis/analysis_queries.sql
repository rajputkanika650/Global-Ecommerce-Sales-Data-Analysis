-- ============================================================
-- GLOBAL E-COMMERCE SALES DATA ANALYSIS
-- SQL ANALYSIS
-- ============================================================

-- Database/Table:
-- global_ecommerce_sales


-- ============================================================
-- 1. TOTAL NUMBER OF RECORDS
-- ============================================================

SELECT COUNT(*) AS Total_Records
FROM global_ecommerce_sales;


-- ============================================================
-- 2. TOTAL ORDERS
-- ============================================================

SELECT COUNT(DISTINCT Order_ID) AS Total_Orders
FROM global_ecommerce_sales;


-- ============================================================
-- 3. TOTAL CUSTOMERS
-- ============================================================

SELECT COUNT(DISTINCT Customer_Name) AS Total_Customers
FROM global_ecommerce_sales;


-- ============================================================
-- 4. TOTAL PRODUCTS
-- ============================================================

SELECT COUNT(DISTINCT Product_Name) AS Total_Products
FROM global_ecommerce_sales;


-- ============================================================
-- 5. TOTAL SALES
-- ============================================================

SELECT SUM(Total_Sales) AS Total_Sales
FROM global_ecommerce_sales;


-- ============================================================
-- 6. TOTAL PROFIT
-- ============================================================

SELECT SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales;


-- ============================================================
-- 7. TOTAL QUANTITY SOLD
-- ============================================================

SELECT SUM(Quantity) AS Total_Quantity
FROM global_ecommerce_sales;


-- ============================================================
-- 8. AVERAGE ORDER VALUE
-- ============================================================

SELECT
    SUM(Total_Sales) / COUNT(DISTINCT Order_ID)
    AS Average_Order_Value
FROM global_ecommerce_sales;


-- ============================================================
-- 9. SALES BY COUNTRY
-- ============================================================

SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM global_ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC;


-- ============================================================
-- 10. TOP 10 COUNTRIES BY SALES
-- ============================================================

SELECT
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM global_ecommerce_sales
GROUP BY Country
ORDER BY Total_Sales DESC
LIMIT 10;


-- ============================================================
-- 11. SALES BY REGION
-- ============================================================

SELECT
    Region,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;


-- ============================================================
-- 12. SALES BY PRODUCT CATEGORY
-- ============================================================

SELECT
    Product_Category,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity) AS Total_Quantity
FROM global_ecommerce_sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC;


-- ============================================================
-- 13. TOP 10 PRODUCTS BY SALES
-- ============================================================

SELECT
    Product_Name,
    SUM(Total_Sales) AS Total_Sales
FROM global_ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;


-- ============================================================
-- 14. TOP 10 PRODUCTS BY PROFIT
-- ============================================================

SELECT
    Product_Name,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;


-- ============================================================
-- 15. LOSS-MAKING PRODUCTS
-- ============================================================

SELECT
    Product_Name,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY Product_Name
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC;


-- ============================================================
-- 16. SALES BY CUSTOMER SEGMENT
-- ============================================================

SELECT
    Customer_Segment,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(DISTINCT Customer_Name) AS Total_Customers
FROM global_ecommerce_sales
GROUP BY Customer_Segment
ORDER BY Total_Sales DESC;


-- ============================================================
-- 17. TOP 10 CUSTOMERS BY SALES
-- ============================================================

SELECT
    Customer_Name,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY Customer_Name
ORDER BY Total_Sales DESC
LIMIT 10;


-- ============================================================
-- 18. SALES BY PAYMENT METHOD
-- ============================================================

SELECT
    Payment_Method,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;


-- ============================================================
-- 19. YEAR-WISE SALES
-- ============================================================

SELECT
    EXTRACT(YEAR FROM Order_Date) AS Year,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY EXTRACT(YEAR FROM Order_Date)
ORDER BY Year;


-- ============================================================
-- 20. MONTH-WISE SALES
-- ============================================================

SELECT
    EXTRACT(MONTH FROM Order_Date) AS Month,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY EXTRACT(MONTH FROM Order_Date)
ORDER BY Month;


-- ============================================================
-- 21. QUARTER-WISE SALES
-- ============================================================

SELECT
    EXTRACT(QUARTER FROM Order_Date) AS Quarter,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY EXTRACT(QUARTER FROM Order_Date)
ORDER BY Quarter;


-- ============================================================
-- 22. SALES BY YEAR AND COUNTRY
-- ============================================================

SELECT
    EXTRACT(YEAR FROM Order_Date) AS Year,
    Country,
    SUM(Total_Sales) AS Total_Sales
FROM global_ecommerce_sales
GROUP BY
    EXTRACT(YEAR FROM Order_Date),
    Country
ORDER BY Year, Total_Sales DESC;


-- ============================================================
-- 23. PROFIT MARGIN BY CATEGORY
-- ============================================================

SELECT
    Product_Category,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / NULLIF(SUM(Total_Sales), 0)) * 100
        AS Profit_Margin_Percent
FROM global_ecommerce_sales
GROUP BY Product_Category
ORDER BY Profit_Margin_Percent DESC;


-- ============================================================
-- 24. DISCOUNT ANALYSIS
-- ============================================================

SELECT
    Discount_Percent,
    COUNT(*) AS Total_Orders,
    SUM(Total_Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM global_ecommerce_sales
GROUP BY Discount_Percent
ORDER BY Discount_Percent;


-- ============================================================
-- 25. SHIPPING COST BY COUNTRY
-- ============================================================

SELECT
    Country,
    SUM(Shipping_Cost) AS Total_Shipping_Cost,
    SUM(Total_Sales) AS Total_Sales
FROM global_ecommerce_sales
GROUP BY Country
ORDER BY Total_Shipping_Cost DESC;


-- ============================================================
-- 26. AVERAGE PRODUCT PRICE BY CATEGORY
-- ============================================================

SELECT
    Product_Category,
    AVG(Unit_Price) AS Average_Unit_Price
FROM global_ecommerce_sales
GROUP BY Product_Category
ORDER BY Average_Unit_Price DESC;


-- ============================================================
-- 27. HIGH-VALUE ORDERS
-- ============================================================

SELECT
    Order_ID,
    Customer_Name,
    Country,
    Product_Name,
    Total_Sales,
    Profit
FROM global_ecommerce_sales
WHERE Total_Sales >
(
    SELECT AVG(Total_Sales)
    FROM global_ecommerce_sales
)
ORDER BY Total_Sales DESC;


-- ============================================================
-- 28. TOP 5 CUSTOMERS IN EACH COUNTRY
-- ============================================================

WITH CustomerSales AS
(
    SELECT
        Country,
        Customer_Name,
        SUM(Total_Sales) AS Total_Sales,
        ROW_NUMBER() OVER
        (
            PARTITION BY Country
            ORDER BY SUM(Total_Sales) DESC
        ) AS Rank_No
    FROM global_ecommerce_sales
    GROUP BY Country, Customer_Name
)

SELECT
    Country,
    Customer_Name,
    Total_Sales,
    Rank_No
FROM CustomerSales
WHERE Rank_No <= 5
ORDER BY Country, Rank_No;


-- ============================================================
-- 29. TOP PRODUCT IN EACH CATEGORY
-- ============================================================

WITH ProductSales AS
(
    SELECT
        Product_Category,
        Product_Name,
        SUM(Total_Sales) AS Total_Sales,
        ROW_NUMBER() OVER
        (
            PARTITION BY Product_Category
            ORDER BY SUM(Total_Sales) DESC
        ) AS Rank_No
    FROM global_ecommerce_sales
    GROUP BY Product_Category, Product_Name
)

SELECT
    Product_Category,
    Product_Name,
    Total_Sales
FROM ProductSales
WHERE Rank_No = 1
ORDER BY Total_Sales DESC;


-- ============================================================
-- 30. CATEGORY CONTRIBUTION TO TOTAL SALES
-- ============================================================

SELECT
    Product_Category,
    SUM(Total_Sales) AS Category_Sales,

    ROUND(
        (
            SUM(Total_Sales) * 100.0
            /
            (SELECT SUM(Total_Sales)
             FROM global_ecommerce_sales)
        ),
        2
    ) AS Sales_Percentage

FROM global_ecommerce_sales

GROUP BY Product_Category

ORDER BY Sales_Percentage DESC;


-- ============================================================
-- 31. REGION CONTRIBUTION TO TOTAL SALES
-- ============================================================

SELECT
    Region,
    SUM(Total_Sales) AS Region_Sales,

    ROUND(
        (
            SUM(Total_Sales) * 100.0
            /
            (SELECT SUM(Total_Sales)
             FROM global_ecommerce_sales)
        ),
        2
    ) AS Sales_Percentage

FROM global_ecommerce_sales

GROUP BY Region

ORDER BY Sales_Percentage DESC;


-- ============================================================
-- 32. FINAL BUSINESS SUMMARY
-- ============================================================

SELECT

    SUM(Total_Sales) AS Total_Sales,

    SUM(Profit) AS Total_Profit,

    SUM(Quantity) AS Total_Quantity,

    COUNT(DISTINCT Order_ID) AS Total_Orders,

    COUNT(DISTINCT Customer_Name) AS Total_Customers,

    COUNT(DISTINCT Product_Name) AS Total_Products,

    ROUND(
        SUM(Profit) * 100.0 /
        NULLIF(SUM(Total_Sales), 0),
        2
    ) AS Profit_Margin_Percent

FROM global_ecommerce_sales;