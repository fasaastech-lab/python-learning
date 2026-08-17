rivers = {'Nile': 'Egypt',
          'Amazon': 'Peru',
          'Mississipi': 'USA',}

for river, location in rivers.items():
    print(f'The {river} runs through {location}.')

for river in rivers:
    print(f'{river}')

for location in rivers.values():    
    print(f'{location}')

