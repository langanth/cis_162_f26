import random
'''
health = 100
hits = 0

while health > 0:
    health -= random.randint(1, 20)
    print(health)
print('now your character is unalived')'''

total = 0
values = 0
ui = input('Please provide an integer or q to quit')

while ui != 'q':
    val = int(ui)
    total += val
    values += 1
    ui = input('Please provide an integer or q to quit')

if values == 0:
    values = 1
print(f'The average value of the numbers you entered is {total / values}')