"""
create a function that given an integer,
creates a nested list with that many
lists, containing the same number of 0s inside

i.e. 
nested_lst(3) -> [[0, 0, 0], [0, 0, 0]. [0, 0, 0]]
nested_lst(1) -> [[1]]
nested_lst(0) -> []
nested_lst(2) -> [[0, 0], [0, 0]]
"""

def nested_lst(val):
    pass

"""
create a string that represents a grid of seats
for a movie theatre. Given are a string of 
letters to represent each row, and a number to
represent the number of columns.

i.e.
theatre_seating('ABC', 3)
'A1    A2    A3
 B1    B2    B3
 C1    C2    C3
"""

def theatre_seating(st, num):
    pass

"""
Given two integers, display a multiplication table

i.e. mult_table(2, 3)

X   1   2   3
1   1   2   3
2   2   4   6

"""
def mult_table(x, y):
    pass

print(theatre_seating('abc', 3))
print(mult_table(4, 5))
print(nested_lst(3))