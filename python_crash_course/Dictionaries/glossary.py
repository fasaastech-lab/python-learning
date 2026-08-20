glossary = {
    'Functions': 'verbs that tells Python what to do',
    'Arguments': 'give context to functions',
    'Side effects': 'results of implementing functions',
    'Strings': 'texts enclosed in quote',
    'Bool': 'determines if statements are True or False'
    }
glossary['Parameters'] = 'variables in functions definition'
glossary['Index'] = 'the position of items in a sequence'
glossary['Slice'] = 'part of a sequence'
glossary['Syntax'] = 'rules governing how Python code is written'
glossary['Variables'] = 'named containers used to store data'

for words, meaning in sorted(glossary.items()):
    print(f"{words}:\n\t{meaning}\n")
