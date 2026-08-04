indexed_colors={1:"red", 2:"green", 3:"blue"}

print(indexed_colors)  

for key in indexed_colors:
    print(key, indexed_colors[key])

for key, value in indexed_colors.items():
    print(key, value)

print(len(indexed_colors))  # Output: 3

indexed_colors[4]="yellow"  # Adds a new key-value pair
print(indexed_colors)  # Output: {1: 'red', 2: 'green', 3: 'blue', 4: 'yellow'}