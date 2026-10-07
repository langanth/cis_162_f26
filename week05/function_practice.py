"""
Given a string name, return a greeting, "Bob"
with "Hello NAME" -> "Hello Bob"
"""

def greeting(st):
    return "Hello " + st


"""
Given a string of even length, write a function
that returns the first half of the string 

first_half("HelloThere") -> "Hello"
"""

def first_half(msg):
    l = len(msg)
    m = l // 2
    return msg[:m]

"""
You are driving a little too fast, and a 
police officer stops you. 
Write code to compute the result, 
encoded as an int value: 
0=no ticket, 1=small ticket, 2=big ticket. 
If speed is 60 or less, the result is 0. 
If speed is between 61 and 80 inclusive, the result is 1. 
If speed is 81 or more, the result is 2. 
Unless it is your birthday -- 
on that day, your speed can be 5 higher in all cases.
"""

def caught_speeding(speed, birthday):
    ticket = 0
    bump = 0

    if birthday:
        bump = 5

    if 61 + bump <= speed <= 80 + bump:
        ticket = 1
    elif 81 + bump <= speed:
        ticket = 2
    return ticket