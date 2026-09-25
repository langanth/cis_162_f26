"""Given the two inputs par and strokes, determine
the scores name in golf.

"Eagle": Two strokes less than par
"Birdie": One stroke less than par
"Par": Number of strokes equals par
"Bogey": One stroke more than par
"Oof": Two or more strokes than par
"""

par = int(input('What is the par for this hole?: '))
strokes = int(input('How many strokes were taken when playing this hole?: '))

