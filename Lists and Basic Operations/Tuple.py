# Exercise 19: Tuple Immutability Test
# Create a tuple: dimensions = (1920, 1080)
# Try to change the first value (should fail)
# Then create a new tuple with different values
# Your code here:
dimensions = (1920, 1080)

# Trying to change the first value
#dimensions[0] = 1020
#print(dimensions)
# Trying to change the first value (will fail)
try:
    dimensions[0] = 1020
except TypeError:
    print("Cannot change a tuple! Tuples are immutable.")

# Creating a new tuple with different values
dimensions = (1020, 1080)
print(dimensions)