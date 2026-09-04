#implement the decorator that caches the return values of the function so that when it is call with the same argument the cached value is returned instead of reexecuting the function.

import time

def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            print(f"Returning cached value for {func.__name__} with arguments: {args}, {kwargs}")
            return cache_dict[args]
        result=func(*args, **kwargs)
        cache_dict[args] = result   
        return result
    return wrapper

    
@cache
def long_running_function(a, b):
    time.sleep(4)  # Simulate a long-running operation
    return a + b

print(long_running_function(2, 3))  # This will take 4 seconds to execute
print(long_running_function(2, 3))  # This will return the cached value immediately
print(long_running_function(5, 7))  # This will take 4 seconds to execute
print(long_running_function(5, 7))  # This will return the cached value immediately
