# Exercise 37: Login System
# usernames = ['admin', 'teacher', 'student']
# input_user = 'teacher'
# If user in list: print "Welcome [user]"
# If user is 'admin': print special admin message
# If not in list: print "Access denied"
# Your code here:
usernames = ['admin', 'teacher', 'student']
input_user = 'teacher'
if input_user in usernames:
    print('Welcome', input_user)

    if input_user == 'admin':
        print("Access Granted")
    else:
        print('Contact Admin')
else:
    print('Access denied!')