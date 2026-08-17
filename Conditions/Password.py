# Exercise 33: Password Validator
# password = "12345"
# Check if password:
# - Is at least 8 characters
# - Contains a number
# Print "Valid" or "Invalid"
# Your code here:

password = "1234567"

is_long_enough = len(password) > 7
has_number = False
for character in password:
    if character.isdigit():
        has_number = True

if is_long_enough and has_number:
    print("Valid")
else:
    print("Invalid")