-- Total sales by category
SELECT Category, SUM(Sales) AS total_sales
FROM cleaned_superstore_sales
GROUP BY Category
ORDER BY total_sales DESC;

-- Monthly sales trend
SELECT order_month, SUM(Sales) AS monthly_sales
FROM cleaned_superstore_sales
GROUP BY order_month
ORDER BY order_month;

-- Sales by region
SELECT Region, SUM(Sales) AS total_sales
FROM cleaned_superstore_sales
GROUP BY Region
ORDER BY total_sales DESC;

-- Top 10 products by sales
SELECT Product_Name, SUM(Sales) AS total_sales
FROM cleaned_superstore_sales
GROUP BY Product_Name
ORDER BY total_sales DESC
LIMIT 10;
