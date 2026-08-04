# This program takes a grade as input and prints a corresponding message based on the grade.
grade=input("Enter your grade:")

if grade=="A" or grade=="a":
    print("Excellent!")
if grade=="B" or grade=="b":
    print("Well done!")
if grade=="C" or grade=="c":
    print("Good!")
if grade=="D" or grade=="d":
    print("You passed.")
if grade=="F" or grade=="f":
    print("Failed...")
else:
    print("Invalid grade entered.")
