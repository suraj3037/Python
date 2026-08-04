weather=input("Enter the weather condition (sunny, rainy, snowy): ")

if weather.lower()=="sunny":
    print("It's a great day for outdoor activities!")
elif weather.lower()=="rainy":
    print("You might want to stay indoors or carry an umbrella.")
elif weather.lower()=="snowy":
    print("Make sure to dress warmly and be careful on the roads.")
else:
    print("Weather condition not recognized. Please enter sunny, rainy, or snowy.")