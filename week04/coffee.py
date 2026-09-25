"""
If a student is tired and has money
they will purchase a coffee
"""

tired = input('are you tired? (y/n): ')
money = input('do you have money? (y/n): ')

if tired.lower() == 'y':
    if money.lower() == 'y':
        print('coffee')
    else:
        print('no coffee')
else:
    print('no coffee')

if tired.lower() == 'y' and money.lower() == 'y':
    print('coffee')
else:
    print('no coffee')