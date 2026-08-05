input_str= input("Enter a string: ")

for char in input_str:
    if input_str.count(char)==1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found.")