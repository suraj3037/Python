fruit='Banana'
color=input("Enter the color of the fruit: ")

if fruit=='Banana' and color.lower()=='yellow':
    print("The banana is ripe.")
    

elif fruit=='Banana' and color.lower()=='green':
    print("The banana is not ripe.")
    

elif fruit=='Banana' and color.lower()=='brown':
    print("The banana is overripe.")

else:
    print("The fruit is not a banana or the color is not recognized.")