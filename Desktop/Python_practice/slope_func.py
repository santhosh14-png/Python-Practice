def calculate_slope(x1,x2,y1,y2):
    if x2==x1:
        print("Vertical line,undefined slope")
    else:
        slope=(y2-y1)/(x2-x1)
    return slope

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

print("Slope is",calculate_slope(x1,x2,y1,y2))
