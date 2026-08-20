# Exercise 1: Name Formatter
# Create variables for first_name, middle_name, last_name
# Print them in different formats:
# - Full name in title case
# - Initials (e.g., A.O.F.)
# - Last name, First name format
# - All uppercase
# Your code here:


first_name = "abdulraheem"
middle_name = "kehinde"
last_name = "fasasi"

# Full name in title case
print(f"{first_name.title()} {middle_name.title()} {last_name.title()}")

# Initials
print(f"{first_name[0].upper()}.{middle_name[0].upper()}.{last_name[0].upper()}.")

# Last name, First name format
print(f"{last_name.title()}, {first_name.title()} {middle_name.title()}")

# All uppercase
print(f"{first_name.upper()} {middle_name.upper()} {last_name.upper()}")
