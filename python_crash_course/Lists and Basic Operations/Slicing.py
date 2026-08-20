# Exercise 20: List Slicing Mastery
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Print:
# - First 3 numbers
# - Middle 4 numbers
# - Last 3 numbers
# - Every 2nd number
# - Numbers in reverse
# Your code here:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('First 3 numbers:', numbers[:3])
print('Middle 4 numbers:', numbers[3:7])
print('Last 3 numbers:', numbers[-3:])
print('Every 2nd number:', numbers[::2])
print("Numbers in reverse:",numbers[::-1])