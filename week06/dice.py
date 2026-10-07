import random

def roll_die(sides):
    return random.randint(1, sides)


r1 = roll_die(6)
r2 = roll_die(6)
print(r1, r2, r1 + r2)

x = 0
while x < 10:
    print(x)
    x = x + 1
    # x += 1

print('loop complete')