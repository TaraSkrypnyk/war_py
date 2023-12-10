try:
    number1 = float(input("Enter number: "))
    number2 = float(input("Enter number: "))
    if (number1 <= number2):
        print(number2)
    else:
        print(number1)
except Exception as e:
    print (e)
