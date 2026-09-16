-- Total Revenue
SELECT SUM(total_amount) AS total_revenue
FROM orders;


-- Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- Average Order Value
SELECT AVG(total_amount) AS average_order_value
FROM orders;


-- Revenue by Product
SELECT
    product,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY product
ORDER BY revenue DESC;


-- Revenue by Region
SELECT
    region,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY region
ORDER BY revenue DESC;


-- Daily Revenue
SELECT
    order_date,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY order_date
ORDER BY order_date;