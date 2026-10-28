"""
Given a number between 11 and 99 inclusively
return the first number to have the same 
first and second digit

countdown(87) -> 77
countdown(98) -> 88
countdown(30) -> 22

"""

def countdown(num):
    for i in range(num, 10, -1):
        st = str(i)
        if st[0] == st[1]:
            return i


print(countdown(86))
print(countdown(74))
print(countdown(15))