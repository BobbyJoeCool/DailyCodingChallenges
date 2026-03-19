-- Challenge: High-Value Orders
-- Difficulty: Beginner
--
-- Standard Rules:
-- 1. ALWAYS include database setup
-- 2. Drop only tables used in this challenge
--
-- Scenario:
-- You are working in a warehouse system and need to identify larger orders.
--
-- Task:
-- Write a query to find all orders where the order_total is GREATER THAN 100.
--
-- Requirements:
-- 1. Return: order_id, customer_id, order_total
-- 2. Only include orders with order_total > 100
-- 3. Sort results by order_total in DESCENDING order
--
-- ============================================
-- DATABASE SETUP (ALWAYS INCLUDED)
-- ============================================
CREATE DATABASE IF NOT EXISTS daily_challenge;
USE daily_challenge;

-- ============================================
-- TABLE SETUP
-- ============================================
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_total DECIMAL(6,2)
);

INSERT INTO orders (order_id, customer_id, order_total) VALUES
(1, 1, 50.00),
(2, 1, 200.00),
(3, 2, 75.00),
(4, 3, 150.00),
(5, 3, 20.00),
(6, 4, 300.00);

-- ============================================
-- YOUR QUERY BELOW
-- ============================================

SELECT * FROM orders
WHERE order_total > 100
ORDER BY order_total DESC;

-- ============================================
-- EXPECTED RESULT (MySQL)
-- ============================================
-- order_id | customer_id | order_total
-- ---------|-------------|------------
--    6     |      4      |   300.00
--    2     |      1      |   200.00
--    4     |      3      |   150.00