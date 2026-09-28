"""
write a function called  check win.
if all three integers match return 20
if two integers match return 10
all other cases return 0
"""
from random import randint

def gen_nums():
    return randint(1, 10)

def check_win(a, b, c):
    if a == b == c:
        return 20
    elif a == b or c == b or a == c:
        return 10
    return 0

