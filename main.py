try:
    number1 = float(input("Enter number: "))
    if (number1 < 0):
        print("Error")
    else:
        if (number1 % 7 == 0):
            print(number1, "Number is a multiple of 7")
        else:
            print(number1, "Number is not a multiple of 7")
except Exception as e:
    print (e)
