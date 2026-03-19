# Challenge: Package Weight Classifier
# Difficulty: Beginner
#
# In a warehouse environment, packages must be classified before shipping.
# Your task is to write a function that takes a package weight (in pounds)
# and returns both its classification and shipping cost.
#
# Classification Rules:
# - 0 < weight <= 1       → "Light"
# - 1 < weight <= 5       → "Standard"
# - 5 < weight <= 20      → "Heavy"
# - weight > 20           → "Oversized"
#
# Shipping Cost Rules:
# - Light       → $3
# - Standard    → $7
# - Heavy       → $15
# - Oversized   → $25 + $0.50 per pound over 20
#
# Edge Cases:
# - If weight is 0 or negative → return "Invalid weight"
#
# Return Format:
# - If valid: return a tuple → (classification, cost)
#   Example: ("Standard", 7)
#
# - If invalid: return string → "Invalid weight"
#
# Notes:
# - Round cost to 2 decimal places if needed
# - Do NOT print inside the function

def classify_package(weight):
    weight_class = ""
    cost = 0
    if weight <= 0:
        return "Invalid weight"
    elif weight <= 1:
        weight_class = "Light"
        cost = 3
    elif weight <= 5:
        weight_class = "Standard"
        cost = 7
    elif weight <= 20:
        weight_class = "Heavy"
        cost = 15
    else:
        weight_class = "Oversized"
        cost = 25 + (weight-20) * .5
    
    cost = round(cost, 2)
    
    return (weight_class, cost)


if __name__ == "__main__":
    print(classify_package(0.5))   # Expected: ("Light", 3)
    print(classify_package(3))     # Expected: ("Standard", 7)
    print(classify_package(10))    # Expected: ("Heavy", 15)
    print(classify_package(25))    # Expected: ("Oversized", 27.5)
    print(classify_package(-2))    # Expected: "Invalid weight"