topping = ""
while topping != 'quit':
    topping = input("Enter a pizza topping: ")
    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza.")


active = True
while active: 
    topping = input("Enter a pizza topping: ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")


while True:
    topping = input("Enter a pizza topping: ")
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")
