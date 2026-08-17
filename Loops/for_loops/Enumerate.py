# Exercise 26: Enumerate Practice
# students = ['Aisha', 'Bilal', 'Fatima']
# Print with roll numbers:
# Roll #1: Aisha
# Roll #2: Bilal
# Roll #3: Fatima
# Your code here:
students = ['Aisha', 'Bilal', 'Fatima']

# Method 1:
for i, student in enumerate(students):
    print(f"Roll #{i+1}: {student}")

    
# Method 2
for i in range(len(students)):
    print(f"Roll #{i+1}: {students[i]}")