password = input("Enter your password: ")

if len(password) < 6:
    print("Weak Password")
elif len(password)< 8:
    print("Moderate Password")
else:
    print("Strong Password")