# Exercise 32: Age Category
# age = 25
# Print category:
# - Child (0-12)
# - Teenager (13-19)
# - Adult (20-59)
# - Senior (60+)
# Your code here:
age = 25
if age < 13:
    print("Child")
elif age < 20:
    print('Teenager')
elif age < 60:
    print('Adult')
else: 
    print('Senior')