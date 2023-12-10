try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    number3 = float(input("Enter third number: "))
    print("Sum", number1 + number2 + number3)
    print("Product", number1 * number2 * number3)
except Exception as e:
    print (e)
