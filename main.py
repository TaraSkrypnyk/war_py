try:
    number1 = float(input("Введіть овжину першої діагоналі: "))
    number2 = float(input("Введіть довжину другої діагоналі : "))
    number3 = 2
    if (number1 <= 0 or number2 <= 0):
        print("Error")
    else:
        print("Площа дорівнює", number1 * number2 / number3)
except Exception as e:
    print (e)
