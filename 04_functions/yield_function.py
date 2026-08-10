def even_printer(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_printer(10):
    print(num)  # Output: 0, 2, 4, 6, 8, 10