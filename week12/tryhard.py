while True:
    try:
        a = int(input("Please enter an integer: "))
        b = int(input("Please enter another integer: "))
        if a < 0 or b < 0:
            raise ValueError
        total = a / b
        print(total)

    except ZeroDivisionError:
        print("We cannot divide by zero!")
        print("PLEASE TRY AGAIN!")
    except ValueError:
        print("You did not provide a positive integer!")
        print("please don't do that again.")
    except:
        print("stop breaking stuff")
        print("please try again!")