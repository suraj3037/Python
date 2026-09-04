#Create the decoratoer that prints the function name and the the value of the arguments every time the function is called.

def debug_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@debug_calls
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")