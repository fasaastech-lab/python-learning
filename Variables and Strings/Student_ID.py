# Exercise 6: Student ID Generator
# Given: first_name = "aisha", last_name = "abdullah", grade = "jss2"
# Generate ID: VEA-JSS2-AIS-ABD (school-grade-first3-last3)
# Your code here:
first_name = "aisha" 
last_name = "abdullah"
grade = "jss2"
school = "VEA"

student_id = f"{school}-{grade.upper()}-{first_name[:3].upper()}-{last_name[:3].upper()}"
print(student_id)