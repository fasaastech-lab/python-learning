people = [
    {
        "first_name": "Hafsah",
        "last_name": "Adenekan",
        "age": 28,
        "city": "Lagos"
     },
    {
        "first_name": "Kifaayah",
        "last_name": "Zakariyyah",
        "age": 26,
        "city": "Akure"
    },
    {
        "first_name": "Maryam",
        "last_name": "Fasasi",
        "age": 33,
        "city": "Ogun"
    },
]
for person in people:
    print("Person's Details:")
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()
