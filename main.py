try:
    number1 = float(input("Enter number: "))
    number2 = float(input("Enter percent: "))
    number3 = 100;
    if (number2 <= 0):
        print("Error")
    else:
        print("Result", number1 / number3 * number2)
except Exception as e:
    print (e)
