quit = 'no'
while True:
    if quit == 'yes':
        break
    age = int(input("Enter your age: "))
    if age < 3:
        ticket = 0
        print('Your ticket is free')
    elif age < 12:
        ticket = 10
        print(F'Your ticket is ${ticket}')
    else:
        ticket = 15
        print(F'Your ticket is ${ticket}')
    quit = input("Do you want to quit yes/no ")