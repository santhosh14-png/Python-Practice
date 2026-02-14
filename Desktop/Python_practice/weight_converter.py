w=float(input("Enter your weight:"))
unit=input("Enter the units(kg/lb):")

if unit=="kg":
    w*=2.205
    print("Your weight is pounds is ",w,"lbs")
elif unit=="lb":
    w/=2.205
    print(f"Your weight in kilograms is {round(w,2)} kgs")
else:
    print("Invalid input")

