try:
    number1 = float(input("Введіть овжину однієї сторони прямокутника: "))
    number2 = float(input("Введіть довжину другої сторони прямокутника : "))
    if (number1 <= 0 or number2 <= 0):
        print("Error")
    else:
        print("Площа дорівнює", number1 * number2)
except Exception as e:
    print (e)
