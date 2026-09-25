"""
Squirrels like to play outside as long as it is between 60 and 90 (inclusively).
Unless it is summer, then it has an upperbound of 100 (inclusively):

print True if they are going to play outside, otherwise print False
"""

temp = int(input('Please enter a temp: '))
is_summer = input('Is it summer?: ')

if is_summer.lower() == 'y':
    #print(60 <= temp <= 100)
    #if 60 <= temp and temp <= 100:
    if 60 <= temp <= 100:
        print(True)
    else:
        print(False)
else:
    #print(60 <= temp <= 90)
    if 60 <= temp <= 90:
        print(True)
    else:
        print(False)