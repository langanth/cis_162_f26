

def squirrels(temp, is_summer):
    if is_summer.lower() == 'y':
        #print(60 <= temp <= 100)
        #if 60 <= temp and temp <= 100:
        if 60 <= temp <= 100:
            return True
        else:
            return False
    else:
        #print(60 <= temp <= 90)
        if 60 <= temp <= 90:
            return True
        else:
            return False


while True:
    temp = int(input('Please enter a temp: '))
    is_summer = input('Is it summer?: ')
    result = squirrels(temp, is_summer)
    print(result)
    print(squirrels(temp, is_summer))