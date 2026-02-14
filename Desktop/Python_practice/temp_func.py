def temp_convert(temp,unit):
    if unit=="C":
        temp=(temp*(9/5))+32
        unit='F'
        print(f"Temperature is farenheit is {round(temp,2)} {unit}")

    elif unit=="F":
        temp=(temp-32)*(5/9)
        unit="C"
        print(f"Temperature is celsius is {round(temp,2)} {unit}")

    else:
        print("Invalid input")

tem=float(input("Enter the temperature:"))
uni=input("Enter the units:")
temp_convert(tem,uni)