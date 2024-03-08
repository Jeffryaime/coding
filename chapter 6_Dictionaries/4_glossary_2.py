glossary = {
    'variable': 'a named storage for data that can change during program execution.',
    'function': 'a code block executed when called, which can perform actions and return results.',
    'loop': 'code that repeats until a condition is met, used for iterating over data.',
    'if statement': 'code that executes based on a true or false condition.',
    'syntax': 'rules defining correct structure of code in a programming language.'
    ''
    }

print("\nHere is the glossary of my 5 learning programming words:\n")
for word,meaning in glossary.items():
    print(f'\t{word.title()}:\n\t{meaning}\n')
    


