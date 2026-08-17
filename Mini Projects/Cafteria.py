"""
School Cafeteria Ordering System

Requirements:
1. Menu with at least 6 items (name and price)
2. Available items list (some items might be sold out)
3. Features:
   - Display menu
   - Take orders (use loop)
   - Check if item available
   - Calculate total
   - Apply discount if total > ₦500

Expected Output:
==========================================
VICTORY ACADEMY CAFETERIA
==========================================
MENU:
1. Rice & Stew - ₦200
2. Jollof Rice - ₦250
3. Beans - ₦150
4. Fried Rice - ₦300
5. Moi-Moi - ₦100
6. Juice - ₦150

Your order: Rice & Stew
Added: Rice & Stew (₦200)

Your order: Pizza
Sorry, Pizza is not available

Your order: Juice
Added: Juice (₦150)

Your order: done

------------------------------------------
Subtotal: ₦350
Discount: ₦0
Total: ₦350
==========================================
"""

# Your code here:
print('='*40)
print('VEA CAFETERIA')
print('='*40)

menu = ['Rice & Stew','Jollof Rice','Beans','Fried Rice','Moi-Moi','Juice']
price = [200, 250, 150, 300, 100, 150]
available_items = ['Rice & Stew','Beans','Juice']

# Display menu
print('MENU:')
for i in range(len(menu)):
    print(f"{i+1}. {menu[i]} - ₦{price[i]}")

print()

order = ['Rice & Stew', 'Pizza', 'Juice']
total = 0

for item in order:
    print("Your order:", item)

    if item in available_items and item in menu:
        index = menu.index(item)
        item_price = price[index]
        total += item_price
        print(f"Added: {item} (₦{item_price})")
    else:
        print(f"Sorry, {item} is not available")

print('-'*40)

# Discount
discount = 0
if total > 500:
    discount = total * 0.1   # 10% discount

final_total = total - discount

print(f"Subtotal: ₦{total}")
print(f"Discount: ₦{discount}")
print(f"Total: ₦{final_total}")
print('='*40)

