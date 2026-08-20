# Exercise 31: Grade Classifier
# score = 87
# Print grade: A(90+), B(80-89), C(70-79), D(60-69), F(<60)
# Your code here:

print('='*20)
print("grade classifier".upper())
print('='*20)

score = 87
if score > 100:
    print('Invalid input')
elif score > 89:
    print("Grade: A")
elif score > 79:
    print("Grade: B")
elif score > 69:
    print("Grade: C")
elif score > 59:    
    print("Grade: D")
else:
    print("Grade: F")