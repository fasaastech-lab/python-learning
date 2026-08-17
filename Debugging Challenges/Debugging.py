# Bug Hunt #1: Indentation Errors
students = ['aisha', 'bilal', 'fatima']

for student in students:
    print(student.title())
print("Welcome to class!")

# Expected: Each student name in title case, then one "Welcome to class!"
# Current: Error! Fix it.

# Bug Hunt #2: Index Error
scores = [85, 92, 78, 88]

print("First score:", scores[0])
print("Last score:", scores[3])
print("Middle scores:", scores[1:3])

# Expected: Print all scores correctly
# Current: Error! Fix it.

# Bug Hunt #3: Type Error
age = 30
name = "Abdulraheem"

message = name + " is " + str(age) + " years old."
print(message)

# Expected: "Abdulraheem is 25 years old."
# Current: Error! Fix it.

# Bug Hunt #4: Logic Error
students = ['aisha', 'bilal', 'fatima', 'yusuf']

for student in students:
    if student == 'bilal':
        print(student.upper())
    else:
        print(student.title())

# Expected: BILAL in caps, others in title case
# Current: Not working as expected. Fix it.

# Bug Hunt #5: List Copy Error
my_subjects = ['Math', 'English', 'Science']
friend_subjects = my_subjects[:]

my_subjects.append('History')
friend_subjects.append('Art')

print("My subjects:", my_subjects)
print("Friend's subjects:", friend_subjects)

# Expected: Different lists
# Current: Both have all subjects! Fix it.

# Bug Hunt #6: Conditional Error
grade = 'jss1'.upper()

if grade == 'JSS1':
    fee = 80000
elif grade == 'JSS2':
    fee = 85000
else:
    fee = 90000

print(f"Fee: ₦{fee:,}")

# Expected: Should work with 'jss1'
# Current: Always goes to else. Fix it.

# Bug Hunt #7: Range Error
for i in range(1, 6):
    print(f"Number: {i}")

# Expected: Print 1, 2, 3, 4, 5
# Current: Doesn't print 5! Fix it.

# Bug Hunt #8: Empty List Error
students = []
if not students:
    print('No students in class')
else:    
    for student in students:
        print(f"Welcome {student}")
    print("Class started!")

# Expected: Should print message if no students
# Current: Just prints "Class started!". Add proper check.

# Bug Hunt #9: Pop Error
numbers = [1, 2, 3, 4, 5]

# Remove first 3 numbers
removed1 = numbers.pop(0)
removed2 = numbers.pop(0)
removed3 = numbers.pop(0)

print("Removed:", removed1, removed2, removed3)
print("Remaining:", numbers)

# Expected: Remove 1, 2, 3; Leave 4, 5
# Current: Wrong numbers removed! Fix it.

# Bug Hunt #10: Syntax Error
prayer_times = ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']

for prayer in prayer_times:
    if prayer == 'Fajr':
        print(prayer + " - Early morning prayer")
    else:
        print(prayer)

# Expected: Special message for Fajr
# Current: Syntax errors! Fix all of them.

# Original Code (works but not optimal)
x = ['aisha', 'bilal', 'fatima']
for _ in x:
    print('Welcome', _.title())

# Your improved version:
# - Use a loop
# - Print in title case
# - Add greeting message

# Original Code (repetitive)
scores = [85, 92]
for score in scores:
    if score>= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    else:
        grade = 'F'
    print('Grade:', grade)
# Your improved version:
# - Use a function (you'll learn this in Ch 8, but try!)
# - Or use a better approach with lists

# Original Code (works but unprofessional)
s=['a','b','c']
for i in s:print(i.upper())

# Your improved version:
# - Proper spacing
# - Better variable names
# - Comments
# - Proper indentation

# Capitalizing alphabets
alphabets = ['a','b','c']
for alphabet in alphabets:
    print(alphabet.upper()) 