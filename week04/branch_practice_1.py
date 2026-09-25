""""
Preferred: f'{value} ... '
Alternative: "{} .... {} ...'.format(val, val2)
"""
val = int(input('Please enter an integer between 0-100: '))
# val = input('Please enter an integer between 0-100: ')

if val > 50:
    print(f'{val} is greater than 50!')

if 25 <= val <= 75:
    print(f'{val} is between 25 and 75!')

print()

if 25 <= val <= 75:
    print(f'{val} is between 25 and 75!')

elif val > 50:
    print(f'{val} is greater than 50!')
