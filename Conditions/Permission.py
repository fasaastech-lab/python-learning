# Exercise 34: Multiple Conditions
# student_age = 16
# has_permission = True
# Check if student can go on trip:
# - Must be 15 or older
# - Must have permission
# Your code here:
student_age = 16
has_permission = True
if student_age > 14 and has_permission == True:
    print('Student can go on trip')
else:
    print('Student cannot go on trip')