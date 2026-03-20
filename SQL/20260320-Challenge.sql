-- Challenge: Customer Spending Summary
-- Difficulty: Beginner → Intermediate
--
-- Standard Rules:
-- 1. ALWAYS include database setup
-- 2. Drop only tables used in this challenge
--
-- Scenario:
-- You need to understand how much each customer has spent in total.
--
-- Task:
-- Write a query to calculate the TOTAL amount spent by each customer.
--
-- Requirements:
-- 1. Return: customer_id, total_spent
-- 2. total_spent = SUM of order_total
-- 3. Group results by customer_id
-- 4. Sort by total_spent in DESCENDING order
--
-- Bonus (Optional):
-- Only include customers who have spent MORE THAN 200 total
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
(5, 3, 100.00),
(6, 4, 300.00);

-- ============================================
-- YOUR QUERY BELOW
-- ============================================



-- ============================================
-- EXPECTED RESULT (MySQL)
-- ============================================
-- customer_id | total_spent
-- ------------|-------------
--      4      |   300.00
--      1      |   250.00
--      3      |   250.00
--      2      |    75.00
--
-- BONUS RESULT (> 200):
-- customer_id | total_spent
-- ------------|-------------
--      4      |   300.00
--      1      |   250.00
--      3      |   250.00