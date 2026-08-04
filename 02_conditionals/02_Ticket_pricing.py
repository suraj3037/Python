# Ticket pricing based on age and day of the week

age= int(input("Enter your age: "))
day= input("Enter the day of the week: ")

if age>=18:
    if day.lower()== "wednesday" or day.lower()== "wed":
        print("Ticket price: $10")
    else:
        print("Ticket price: $20")
else:
    if day.lower()== "wednesday" or day.lower()== "wed":
        print("Ticket price: $5")
    else:
        print("Ticket price: $10")