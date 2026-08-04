name= "John Doe"

print(name)

first_char=name[0]
print("First character:", first_char)
print("Last character:", name[-1])

slice_name=name[0:4]
print("Slice of name:", slice_name)

slice_reverse=name[::-1]
print("Reversed name:", slice_reverse)

slice_middle=name[2:6]
print("Middle slice of name:", slice_middle)

slice_with_step=name[0:7:2]
print("Slice with step:", slice_with_step)