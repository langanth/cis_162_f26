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

# Your Code Here

"""A year in the modern Gregorian Calendar consists of 365 days.
In reality, the earth takes longer to rotate around the sun. 
To account for the difference in time, every 4 years, a leap year
takes place. A leap year is whne a year has 366 days. An extra day,
February 29th. The requirements for a given year to be a leap year are:

1. The year must be divisible by 4

2. If the year is a century year (1700, 1800, etc.), the year must be evenly
divisible by 400; therefore both 1700 and 1800 are not leap years.

Provided a year as an integer output whether or not the year is a 
leap year. The output should look like the following:

Enter year: 1712
1712 - leap year

or

1913
1913 - not a leap year
"""

year = int(input("Enter year: "))

# Your code here


"""Write a program that takes a date as input and outputs the date's
season in the Northern hemisphere. The input is a strong to represent
the month and an int to represent the day.

Ex.
April
11

Output should be:
Spring

The dates for each season in the northern hemisphere are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19

"""

month = input("Please enter a month: ")
day = int(input("Please enter a day: "))
