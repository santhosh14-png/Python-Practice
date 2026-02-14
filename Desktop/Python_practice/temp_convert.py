temp=float(input("Enter the temperature:"))
unit=input("Enter units(C/F):")

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