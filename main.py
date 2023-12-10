try:
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    print("Sum", number1 + number2)
    print("Difference", number1 - number2)
    print("Product", number1 * number2)
except Exception as e:
    print (e)
