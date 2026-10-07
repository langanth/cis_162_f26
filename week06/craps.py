import random

def roll_die(sides):
    return random.randint(1, sides)


r1 = roll_die(6)
r2 = roll_die(6)
total = r1 + r2
goal = total
print(r1, r2, r1 + r2)

if total == 7:
    print('you win!')
elif total == 2 or total == 3 or total == 12:
    print('you lose!')
else:
    print(f'Your goal is to roll: {goal}')
    while total != 7:
        r1 = roll_die(6)
        r2 = roll_die(6)
        total = r1 + r2
        print(r1, r2, total)
        if total == goal:
            print('you win!')
            break
    if total == 7:
        print('sorry you lost, thank you for playing!')
    else:
        print('congrats! thank you for playing!')

