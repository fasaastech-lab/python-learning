#Write a program that:
#Stores student names in a list
#Stores their scores in another list
#Prints each student with their score
#Calculates the average score
#Counts how many students passed (score ≥ 50)

students = ['Aisha', 'Bilal', 'Fatima', 'Yusuf', 'Maryam']
scores = [78, 45, 92, 60, 39]

# 1. Print each student with score
for student, score in zip(students, scores):
    print(f"{student} scored {score}")
# 2. Calculate average score
average_scores = sum(scores)/len(students)
print(average_scores)
# 3. Count how many passed (>=50)
passed = 0
for score in scores:
    if score >= 50:
        passed += 1 
print(passed)

# A list of even numbers from 1-10
even_numbers = []
for number in range(2,11,2):
    even_numbers.append(number)
print(even_numbers)

# Searching for umar
names = ['Ahmed', 'Zainab', 'Khadijah', 'Umar']
for name in names:
    if name == 'Umar':
        print("Found!")

# Star Triangle
for i in range(1,6):
    print("*"*i)

# Max number
numbers = [12, 45, 7, 89, 23]

max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(f"Max number is {max_number}")

# Word counter

sentence = "python is easy and python is powerful"
sentence = sentence.split()
no = 0
for i in sentence:
    if i == 'python':
        no += 1
print(no)
    
