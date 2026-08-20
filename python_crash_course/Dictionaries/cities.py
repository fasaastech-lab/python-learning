cities = {
    'Lagos': {
        'country': 'Nigeria',
        'population': '12.8 million',
        'fact': 'Nigeria’s economic hub'
    },
    'Cairo': {
        'country': 'Egypt',
        'population': '25.6 million',
        'fact': 'Largest city in Africa'
    },
    'Accra': {
        'country': 'Ghana',
        'population': '5.6 million',
        'fact': 'Capital of Ghana'
    }
}
for city, info in cities.items():
    print(f"======{city.upper()}======")

    for key, value in info.items():
        print(f"{key.title()} - {value}")
    print()