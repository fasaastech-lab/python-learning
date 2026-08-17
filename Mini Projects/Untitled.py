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
print('='*40)
print('VEA CAFETERIA')
print('='*40)

menu = ['Rice & Stew','Jollof Rice','Beans','Fried Rice','Moi-Moi','Juice']
price = [200, 250, 150, 300, 100, 150]
available_items = ['Rice & Stew','Beans','Juice']

# Display menu
for item in range(len(menu)):
   print(f"{menu[item]} - ₦{price[item]}")

order = ['Rice & Stew', 'Pizza', 'Juice']
for item in order:
   print(f"\nYour order: {item}")
   if item in available_items:
      print(f"Added: {item}")
   else:
      print(f"Sorry, {item} not available")
    