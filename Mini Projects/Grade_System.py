"""
VICTORY EDUCATIONAL ACADEMY
Student Grade Book System

Requirements:
1. Store list of at least 5 students
2. Each student has:
   - Name
   - Marks in 3 subjects (use list)
3. Features:
   - Calculate average for each student
   - Determine letter grade (A-F)
   - Find class average
   - Find top student
   - Print formatted report

Expected Output:
==========================================
VICTORY EDUCATIONAL ACADEMY
Grade Book Report
==========================================
Name                Average    Grade
------------------------------------------
Aisha               88.3       B
Yusuf               92.7       A
Fatima              76.0       C
------------------------------------------
Class Average: 85.7
Top Student: Yusuf (92.7)
==========================================
"""

# Your code here:
width = 30

print('=' * width)
print('VICTORY EDUCATIONAL ACADEMY'.center(width))
print('Grade Book Report'.center(width))
print('=' * width)

# Assigning students and scores
students = ['Fatima','Messiah','Barnabas','Amina','Blessing']
english_scores = [74, 80, 70, 63, 45]
maths_scores = [80, 84, 72, 60, 32]
science_scores = [79, 70, 82, 68, 40]

averages = []
grades = []
#Calculating average for each student
for i in range(len(students)):
   average = (english_scores[i]+maths_scores[i]+science_scores[i])/3
   averages.append(average)
# Determining grades
      
   if average >= 80:
      grade = 'A'
   elif average >= 60:
      grade = 'B'
   elif average >= 50:
      grade = 'C'
   else:
      grade = 'F'
      
   grades.append(grade)
# Class Average
class_average = (sum(averages)/len(students))

# calculating top student
top_student = 0
for i in range(len(averages)):
   if averages[i] > top_student:
      top_student = averages[i]
   
print(f'{'Name':<15}{'Average':<10}{'Grade'}')
print('-'*30)
for i in range(len(students)):
   print(f"{students[i]:<15}{averages[i]:<10.2f}{grades[i]}")
print('-'*30)
print(f"Class average: {class_average}")
print(f"Top student: {top_student}")   
