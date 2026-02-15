name=input("Enter username:")

if len(name)>12:
    print("Must be 12 characters only")
elif not name.find(" ")== -1:
    print("Cannot contain spaces")
elif not name.isalpha:
    print("Cannot contain numbers")
else:
    print("Valid username")