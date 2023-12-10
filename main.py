try:
    number1 = float(input("Введіть свою зп за місяць: "))
    number2 = float(input("Введіть суму місячного платежу за кредитом : "))
    number3 = float(input("Введіть заборгованість за комунальні посмлуги: "))
    if (number1 < 0 or number2 < 0 or number3 < 0):
        print("Error")
    else:
        print("Залишок", number4=number1 - number2 - number3)

except Exception as e:
    print (e)
