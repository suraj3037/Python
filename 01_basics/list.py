colors=['red', 'green', 'blue', 'yellow', 'purple']

print(colors[0])  # Output: red
print(colors[-1])  # Output: purple

print(colors[1:4])  # Output: ['green', 'blue', 'yellow']

for color in colors:
    print(color, end=" ")

print("")

colors[0]='orange'
print(colors)  # Output: ['orange', 'green', 'blue', 'yellow', 'purple']

colors[1:2]=['pink', 'cyan']
print(colors)  # Output: ['orange', 'pink', 'cyan', 'blue', 'yellow', 'purple']

if 'blue' in colors:
    print("Blue is in the list")

colors.append('black')
print(colors) 

print("The popped color is:", colors.pop())  # Removes and returns the last item

colors.remove('pink')  # Removes the first occurrence of 'pink'
print(colors)  # Output: ['orange', 'cyan', 'blue', 'yellow',

colors.sort()  # Sorts the list in ascending order

colors.reverse()  # Reverses the order of the list

colors.clear()  # Removes all items from the list

colors.insert(1, 'white')  # Inserts 'white' at index 1