-- Challenge: Customer Order Summary
-- Difficulty: Beginner
--
-- Your task is to summarize how many orders each customer has placed.
--
-- Requirements:
-- 1. Return each customer_id
-- 2. Count how many orders each customer has placed
-- 3. Name the count column "total_orders"
-- 4. Sort the results by total_orders in DESCENDING order
--
-- Bonus (Optional):
-- Only include customers who have placed MORE THAN 1 order

-- Ensure database exists
CREATE DATABASE IF NOT EXISTS daily_challenge;
USE daily_challenge;

-- Clean table setup
DROP TABLE IF EXISTS orders;

-- Create table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

-- Insert sample data
INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 1, '2024-01-01'),
(2, 1, '2024-01-05'),
(3, 2, '2024-01-03'),
(4, 3, '2024-01-02'),
(5, 3, '2024-01-06'),
(6, 3, '2024-01-10'),
(7, 4, '2024-01-07');

-- ============================================
-- YOUR QUERY BELOW
-- ============================================

SELECT 
    customer_id,
    COUNT(*) AS total_orders
FROM orders
-- WHERE ...
GROUP BY customer_id
-- HAVING ...
ORDER BY total_orders DESC;