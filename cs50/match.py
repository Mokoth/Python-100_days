name = input("Enter name: ")

if name == "Mary" or name == 'Mark' or name == 'Morten':
    print('Gryffindor')
elif name == 'Erick':
    print('Slytherin')
else:
    print('Who?')

# using match
match name:
    case 'Mary':
        print('Gryffindor')
    case 'Mark':
        print('Gryffindor')
    case 'Morten':
        print('Gryffindor')
    case 'Erick':
        print('Slytherin')
    case _:
        print('Who?')

# cleaning
match name:
    case 'Mary' | 'Mark' | 'Morten':
        print('Gryffindor')
    case 'Erick':
        print('Slytherin')
    case _:
        print('Who? ')