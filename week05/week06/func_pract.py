
def even_odd(val):
    eo = False
    if val % 2 == 0:
        eo = True
    return eo

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


def add_even(a, b):
    if even_odd(a):
        return add(a, b)
    return subtract(a, b)

def divide(a, b=1):
    return a / b

print(divide(4))

print(even_odd(3))
print(even_odd(2))




x = 3

if x == 3:
    print(True, 3)
elif x < 5:
    print(True, 5)
elif x == 4:
    print(True, 4)

