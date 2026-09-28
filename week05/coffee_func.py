tired = input('are you tired? (y/n): ')
money = input('do you have money? (y/n): ')

# checks if you're tired
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

def coffee(tired, money):
    if tired.lower() == 'y' and money.lower() == 'y':
        return True
    return False

def coffee2(tired, money):
    return tired.lower() == 'y' and money.lower() == 'y'

