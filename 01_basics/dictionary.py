indexed_colors={1:"red", 2:"green", 3:"blue"}

print(indexed_colors)  

for key in indexed_colors:
    print(key, indexed_colors[key])

for key, value in indexed_colors.items():
    print(key, value)

print(len(indexed_colors))  # Output: 3

indexed_colors[4]="yellow"  # Adds a new key-value pair
print(indexed_colors)  # Output: {1: 'red', 2: 'green', 3: 'blue', 4: 'yellow'}

indexed_colors.pop(4)  # Removes the key-value pair with key 4
print(indexed_colors)  # Output: {1: 'red', 2: 'green', 3: 'blue'}

indexed_colors.popitem()  # Removes the last inserted key-value pair
print(indexed_colors)  # Output: {1: 'red', 2: 'green'}

del indexed_colors[2]  # Deletes the key-value pair with key 2
print(indexed_colors)  # Output: {1: 'red'}


Items={
    "colors": {1: "red", 2: "green", 3: "blue"},
    "fruits": {1: "apple", 2: "banana", 3: "cherry"}
}

print(Items)  # Output: {'colors': {1: 'red', 2: 'green', 3: 'blue'}, 'fruits': {1: 'apple', 2: 'banana', 3: 'cherry'}}

print(Items["colors"][1])  # Output: red
