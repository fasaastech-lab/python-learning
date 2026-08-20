# Exercise 12: List Modification
# Start with: grades = ['A', 'B', 'C', 'D', 'F']
# Add 'A+' at the beginning
# Remove 'F'
# Insert 'B+' after 'A+'
# Print final list
# Your code here:
grades = ['A', 'B', 'C', 'D', 'F']

#Adding 'A+' at the beginning
grades.insert(0, "A+")
print(grades)

# Removing 'F'
del(grades[-1])
print(grades)

# Inserting 'B+' after 'A+'
grades.insert(1, 'B+')
print(grades)
