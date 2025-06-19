-- Sample KPI queries for Power BI/Tableau
-- Total units sold by pattern
SELECT pattern_name, SUM(units_sold) AS total_sold
FROM sales_data
GROUP BY pattern_name;

-- Monthly trend
SELECT pattern_name, DATEPART(MONTH, date) AS month, SUM(units_sold) AS total
FROM sales_data
GROUP BY pattern_name, DATEPART(MONTH, date);
