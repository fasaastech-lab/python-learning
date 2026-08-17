dog = {
    "name": "Buddy",
    "animal": "Dog",
    "owner": "Micheal"
    }
cat = {
    "name": "Mimi",
    "animal": "Cat",
    "owner": "Maryam"
    }
    

parrot = {
    "name": "Coco",
    "animal": "Parrot",
    "owner": "Hafsah"
    }

pets = [dog, cat, parrot]

for pet in pets:
   print("===Pet's Details===")
   print(f"Name: {pet['name']}")
   print(f"Animal: {pet['animal']}")
   print(f"Owner: {pet['owner']}")
   print()

