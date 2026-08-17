# Exercise 35: In-List Check
# subjects = ['Math', 'English', 'Science']
# requested = 'History'
# Check if requested subject is available
# Print appropriate message
# Your code here:
subjects = ['Math', 'English', 'Science']
requested = 'Math'
if requested in subjects:
    print('Requested subject is available')
else:
    print('Requested subject is not available')