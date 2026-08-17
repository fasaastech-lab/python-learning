# Exercise 16: Sorting Challenge
# names = ['Zainab', 'Ahmed', 'Maryam', 'Bilal', 'Fatima']
# Print:
# - Original list
# - Sorted alphabetically (temporary)
# - Original list again (prove it's unchanged)
# - Sorted reverse alphabetically (temporary)
# - Permanently sorted list
# Your code here:
names = ['Zainab', 'Ahmed', 'Maryam', 'Bilal', 'Fatima']
print("Original list:",names)
print("Alphabetical order:",sorted(names))
print("Reverse alphabetically",sorted(names, reverse=True))
names.sort()
print("Permanently sorted list:",names)
