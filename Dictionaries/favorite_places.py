favorite_places = {
    'Abdulrahman': ['Saudi'],
    'Abdulraheem': ['Mecca', 'Medina'],
    'Abdullateef': ['Saudi', 'Canada', 'USA']
    }
for name, place in favorite_places.items():
    if len(place) == 1:
        print(f"{name} favorite place is {place[0]}")
    elif len(place) == 2:
        print(f"{name} favorite place is {place[0]} and {place[1]}")
    else:
        print(f"{name} favorite place is {place[0]}, {place[1]}, and {place[2]}")

# Another way
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name}'s favorite place is {places[0]}.")
    else:
        print(f"{name}'s favorite places are {', '.join(places)}.")