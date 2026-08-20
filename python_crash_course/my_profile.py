# Exercise 1: Your Profile
# Create a dictionary about yourself with:
# - first_name, last_name, age, city, 
#   profession, school_name
# Print each piece of information
# Your code here:

my_profile = {"first_name": "Abdulraheem", "last_name": "Fasasi", "age": 31,
              "city": "Abuja", "profession": "Educator",
              "school_name": "Victory Educational Academy",}

for key, value in my_profile.items():
    print(f"{key}: {value}")
    