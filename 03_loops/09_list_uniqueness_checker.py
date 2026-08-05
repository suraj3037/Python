list1=["apple", "banana", "cherry", "apple", "date", "banana", "fig", "grape", "cherry"]


unique_set= set()

for item in list1:
    if item in unique_set:
        print("Duplicate found:", item)
        break
    else:
        unique_set.add(item)