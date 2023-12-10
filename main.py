try:
    number1 = float(input("Enter number: "))
    if (number1 < 0):
        print("Error")
    else:
        if (number1 % 2 == 0):
            print(number1, "Even number")
        else:
            print(number1, "Odd number")
except Exception as e:
    print (e)
