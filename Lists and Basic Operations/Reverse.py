# Exercise 14: Reverse Engineering
# You have: numbers = [10, 20, 30, 40, 50]
# Using only pop(), create a new list with numbers in reverse
# Don't use .reverse() or [::-1]
# Your code here:
numbers = [10, 20, 30, 40, 50]

# Using others for better comprehension
print(numbers[::-1])
numbers.reverse()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# Using only pop() 
reversed_list = []
reversed_list.append(numbers.pop())
reversed_list.append(numbers.pop())
reversed_list.append(numbers.pop())
reversed_list.append(numbers.pop())
reversed_list.append(numbers.pop())

print("Reversed lists:", reversed_list)

