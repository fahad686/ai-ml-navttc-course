#In Python, a decorator is a powerful design pattern that allows you to add functionality to
# an existing function or class without modifying its source code. This is achieved by "wrapping"
# the original function with another function that takes the original function as an argument and returns
# a new, modified version.
# This is made possible because Python treats functions as first-class
# objects, meaning they can be passed as arguments, assigned to variables, and returned from other
# functions, just like any other data type.


# 1. Define the decorator function
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
        func()
    return wrapper

# 2. Define the function to be decorated
@my_decorator
def say_whee():
    print("Whee!")

@my_decorator
def say_quite():
    print('Keep quite class!')


# 3. Call the decorated function
say_whee()

say_quite()