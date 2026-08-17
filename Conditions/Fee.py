# Exercise 38: Fee Calculator
# grade = 'JSS2'
# siblings = 3
# Calculate fee:
# - Primary: ₦50,000
# - JSS: ₦80,000
# - SSS: ₦100,000
# Discount: 10% per sibling (max 30%)
# Your code here:
grade = 'JSS2'
siblings = 3

#Checking grade
if 'Primary' in grade: 
    fee = 50000
elif 'JSS' in grade: 
    fee = 80000
elif 'SSS' in grade:
    fee = 100000
else:
    print('Invalid grade') 
    exit()

# Calculating discounts
if siblings < 1:
    discount = 0
elif siblings == 1:
    discount = 10/100*fee
elif siblings == 2:
    discount = 20/100*fee
else:
    discount = 30/100*fee

# Payable fees
print(f"Payable fee is ₦{fee-discount}")