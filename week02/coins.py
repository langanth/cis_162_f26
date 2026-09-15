"""
Write a program that takes in the number of quarters, 
dimes, nickels, and pennies. 
Then produce dollar value of all of those coins combined in a print statement.
"""
quarters = int(input('Quarters: '))
dimes = int(input("Dimes: "))
nickels = int(input("Nickels: "))
pennies = int(input("Pennies: "))

dollar = (.25 * quarters) + (.1 * dimes) + (.05 * nickels) + (pennies/100)

print(dollar)