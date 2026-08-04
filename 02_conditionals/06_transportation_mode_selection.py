distance=int(input("Enter the distance to your destination in kilometers: "))

if distance<5:
    print("You can walk to your destination.")
elif distance<20:
    print("You can ride a bicycle to your destination.")
elif distance<100:
    print("You can drive a car to your destination.")
else:
    print("You should consider taking a train or a flight to your destination.")