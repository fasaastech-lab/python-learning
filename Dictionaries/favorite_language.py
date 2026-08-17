favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f'{name.title()} favorite language is {language.title()}\n')

friends = ['sarah', 'phil']
for name in sorted(favorite_languages):
    print(name.title())
    if name in friends:
        print(f'Hi {name} I see your favorite language is '
               f'{favorite_languages[name].title()}')
if 'erin' not in favorite_languages:
    print('Erin, please take our poll')

for language in sorted(set(favorite_languages.values())):
    print(language.title())

poll_names = ['Bello', 'Edward', 'Martins', 'Phil']
for name in poll_names:
    if name.lower() in favorite_languages:
        print(f'{name}, thanks for taking the poll')
    else:
        print(f' {name}, you have not taken the poll')