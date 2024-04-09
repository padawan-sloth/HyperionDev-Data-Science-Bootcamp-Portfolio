menu = ["BLT Sandwich", "Ham Sandwich", "Cheese Sandwich", "Tuna Sandwich", "Coffee", "Tea", "Water", "Juice", "Cake"]  # List of items sold in the cafe

stock = {"BLT Sandwich" : 30, "Ham Sandwich" : 30, "Cheese Sandwich" : 30, "Tuna Sandwich" : 20, "Coffee" : 75, "Tea" : 80, "Water" : 100, "Juice" : 65, "Cake" : 45}   # Stock of each item in the cafe

price = {"BLT Sandwich" : 2.50, "Ham Sandwich" : 2.50, "Cheese Sandwich" : 2.50, "Tuna Sandwich" : 2.50, "Coffee" : 1.50, "Tea" : 1.00, "Water" : 0.50, "Juice" : 1.25, "Cake" : 2.00}  # Price of each item in the cafe

total_stock = 0 # Total value of stock in the cafe

for item in menu:   # For each item in the menu
    item_value = stock[item] * price[item]  # Calculate the value of the stock
    total_stock += item_value   # Add the value of the stock to the total stock

print(total_stock)  # Print the total stock value