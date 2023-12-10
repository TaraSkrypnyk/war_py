try:
    number1 = float(input("Enter number: "))
    number2 = float(input("Enter number: "))
    number3 = 2
    number4 = float(input(
        "Якщо ви хочете побачити суму введіть 1, якщо ви хочите побачити різницю введіть 2, якщо ви хочетет побачити середньоарифметичне введіть три, якщо ви хочете побачити добуток введіть 4 "))
    if (number4 == 1):
        print(number1 + number2)
    elif (number4 == 2):
        print(number1 - number2)
    elif (number4 == 3):
        print((number1 + number2) / number3)
    elif (number4 == 3):
        print(number1 * number2)
    else:
        print("Error")
except Exception as e:
    print (e)
