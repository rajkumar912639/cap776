try :
    divide=10/0
    number=input(int("Enter the number :"))
    print(number)
except ZeroDivisionError as err :
    print(err)
except ValueError:
    print("invalid input ")