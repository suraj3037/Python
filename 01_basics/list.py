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

