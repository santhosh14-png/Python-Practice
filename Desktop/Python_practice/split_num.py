num=int(input("Enter a 6 digit number:"))

n1=num%100
num=num/100

n2=num%100
num=num//100

n3=num%100
num=num//100

print(int(n1))
print(int(n2))
print(int(n3))