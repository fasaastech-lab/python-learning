# ==========================================
# School Cafeteria Ordering System
# ==========================================

# Create the header
print("="*40)
print("VICTORY ACADEMY CAFETERIA")
print("="*40)

# ------------------------------------------
# 1. Menu with 6 items (name and price)
# Using TWO separate lists (like Chapter 3-4)
# ------------------------------------------
menu_items = ["Rice & Stew", "Jollof Rice", "Beans", "Fried Rice", "Moi-Moi", "Juice"]
menu_prices = [200, 250, 150, 300, 100, 150]

# ------------------------------------------
# 2. Available items list (some items sold out)
# "Pizza" is NOT in this list (unavailable)
# ------------------------------------------
available_items = ["Rice & Stew", "Jollof Rice", "Beans", "Fried Rice", "Moi-Moi", "Juice"]

# ------------------------------------------
# Customer's order (pre-made, no input needed)
# You can change these items to test different orders
# ------------------------------------------
order = ["Rice & Stew", "Juice"]

# ------------------------------------------
# Feature: Display menu
# ------------------------------------------
print("MENU:")

# Loop through menu using for loop with range() (like Chapter 4)
for i in range(len(menu_items)):
    print(f"{i+1}. {menu_items[i]} - ₦{menu_prices[i]}")

print()  # Empty line for spacing

# ------------------------------------------
# Feature: Check if items are available
# ------------------------------------------
print("YOUR ORDER:")

# Loop through each item in the order
for item in order:
    # Check if item is in available_items list (using 'in' from Chapter 5)
    if item in available_items:
        print(f"Added: {item}")
    else:
        print(f"Sorry, {item} is not available")

print()

# ------------------------------------------
# Feature: Calculate total
# ------------------------------------------
subtotal = 0  # Start with 0

# Add up all the prices from the order
for item in order:
    # Find the price for this item
    for i in range(len(menu_items)):
        if menu_items[i] == item:
            subtotal += menu_prices[i]
            break

# ------------------------------------------
# Feature: Apply discount if total > ₦500
# ------------------------------------------
if subtotal > 500:
    discount = subtotal * 0.1  # 10% discount (multiply by 0.1)
    total = subtotal - discount  # Subtract discount from subtotal
else:
    discount = 0  # No discount
    total = subtotal  # Total equals subtotal

# ------------------------------------------
# Print summary
# ------------------------------------------
print("-"*40)
print(f"Subtotal: ₦{subtotal}")
print(f"Discount: ₦{discount}")
print(f"Total: ₦{total}")
print("="*40)