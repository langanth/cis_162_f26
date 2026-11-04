"""
Using a nested list as a board,
create a game where players
can take turns placing an 'x' or an 'o'.
After each placement, the program should check
for a winner. When someone wins,
the program should end and declare which player
had won.

You will likely need loops
You may use functions
"""


lst = [['-' for x in range(3)] for _ in range(3)]

x = 0
o = 0

for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 'x':
            x += 1
        elif lst[i][j] == 'o':
            o += 1
