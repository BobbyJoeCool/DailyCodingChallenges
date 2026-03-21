/*
 * Daily Coding Challenge: Inventory Reorder Analyzer
 * Language: Java
 * Difficulty: Intermediate
 *
 * Context:
 * You are building part of a warehouse inventory system. Each product has:
 * - A name
 * - Current stock quantity
 * - Reorder threshold
 * - Cost per unit
 *
 * When stock drops below the reorder threshold, the system should flag the item
 * and calculate how much it would cost to restock it back up to a target level.
 *
 * Your task is to process a list of products and generate a reorder report.
 *
 * Requirements:
 *
 * 1. Create a Product class with:
 *    - String name
 *    - int quantity
 *    - int reorderThreshold
 *    - double costPerUnit
 *
 * 2. Write a function:
 *
 *    public static Map<String, Double> generateReorderReport(List<Product> products, int targetStockLevel)
 *
 *    This function should:
 *
 *    - Identify products where:
 *         quantity < reorderThreshold
 *
 *    - For each of those products:
 *         Calculate how many units need to be ordered:
 *             unitsToOrder = targetStockLevel - quantity
 *
 *         Calculate reorder cost:
 *             reorderCost = unitsToOrder * costPerUnit
 *
 *    - Return a Map where:
 *         Key   = product name
 *         Value = reorder cost
 *
 * 3. Additional Requirements:
 *
 *    - If quantity is already >= targetStockLevel, ignore the product
 *    - Do NOT include products that don't need reordering
 *    - Round cost to 2 decimal places
 *
 * 4. Example:
 *
 * Input:
 * [
 *   ("Widget", 5, 10, 2.50),
 *   ("Gadget", 20, 15, 5.00),
 *   ("Thingamajig", 2, 8, 1.25)
 * ]
 *
 * targetStockLevel = 12
 *
 * Output:
 * {
 *   "Widget": 17.50,       // (12 - 5) * 2.50
 *   "Thingamajig": 12.50   // (12 - 2) * 1.25
 * }
 *
 * Notes:
 * - "Gadget" is NOT included because it is above its reorder threshold
 *
 * Bonus (Optional if you finish early):
 * - Sort the result by highest reorder cost
 * - Return a List of custom objects instead of a Map
 * - Add validation (no negative quantities, etc.)
 */

import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Challenge20260321 {
    static class Product {
        private String name;
        private int quantity;
        private int reorderThreshold;
        private double costPerUnit;

        Product(String name, int quantity, int reorderThreshold, double costPerUnit) {
            this.name = name;
            this.quantity = quantity;
            this.reorderThreshold = reorderThreshold;
            this.costPerUnit = costPerUnit;
        }

        public String getName() {
            return this.name;
        }

        public int getQuantity() {
            return this.quantity;
        }

        public int getReorderThreshold() {
            return this.reorderThreshold;
        }

        public double getCostPerUnit() {
            return this.costPerUnit;
        }
    }

        public static Map<String, Double> generateReorderReport(List<Product> products, int targetStockLevel) {
            if (products == null || products.isEmpty()) {
                return new HashMap<>();
            }
            
            Map<String, Double> reorderList = new HashMap<>();
            for (Product item : products) {
                if (item.getQuantity() < item.getReorderThreshold() && item.getQuantity() < targetStockLevel) {
                    double cost = (targetStockLevel - item.getQuantity()) * item.getCostPerUnit();
                    cost = Math.round(cost * 100.0) / 100.0;
                    reorderList.put(item.getName(), cost);
                }
            }

            return reorderList;
        }
}


