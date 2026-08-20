# Exercise 18: List Copying vs Reference
# original = [1, 2, 3]
# Create TWO variables from original:
# - copy1 (actual copy)
# - copy2 (reference)
# Add 4 to original
# Print all three lists and explain the difference
# Your code here:
original = [1, 2, 3]

# copy1 (actual copy)
copy1 = original[:]
print("Actual copy:", copy1)

# - copy2 (reference)
copy2 = original
print('Reference:', copy2)

# Adding 4 to original
original.append(4)
print("Original list:",original)


score = 25
score = 30
print(score)