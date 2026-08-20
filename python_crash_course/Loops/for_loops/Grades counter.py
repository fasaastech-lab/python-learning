# Exercise 28: Grade Counter
# grades = ['A', 'B', 'A', 'C', 'A', 'B', 'D', 'A']
# Count how many A's are in the list using a loop
# Your code here:
grades = ['A', 'B', 'A', 'C', 'A', 'B', 'D', 'A']
count_A = 0
for grade in grades:
    if grade == 'A':
        count_A += 1
print("Number of A's:",count_A)

