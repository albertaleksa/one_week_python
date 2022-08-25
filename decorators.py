import math
from random import choice
from functools import wraps

# pass one func into another as argument
def my_sum(n, func):
    total = 0
    for el in range(n):
        total += func(el)
    return total


def square(x):
    return x * x


def cube(x):
    return x ^ 3


print(my_sum(3, square))
print(my_sum(3, cube))
print(my_sum(3, math.sqrt))


# nest func inside another func
def greet(person):
    def get_mood():
        msg = choice(("Hi ", "Go away ", "Bye "))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))


# return func from other func
def make_laugh_func():
    def get_laugh():
        l = choice(("Ha-Ha-Ha", "lol", "Te-He-He"))
        return l
    return get_laugh

laugh = make_laugh_func()
print(laugh())


# inner func can access outer func scope
def make_laugh_at_func(person):
    def get_laugh():
        l = choice(("Ha-Ha-Ha", "lol", "Te-He-He"))
        return f"{l} at {person}"
    return get_laugh

laugh_at = make_laugh_at_func("Toby")
print(laugh_at())


#####
def my_greet_func(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I'm a wrapper function"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here is the documentation: {fn.__doc__}")
        return fn(*args, **kwargs).upper()
    return wrapper


@my_greet_func
def greet(name):
    """Return greeting."""
    return f"Hi! My name is {name}."

@my_greet_func
def order(main_dish, side):
    """Return order"""
    return f"I'd like the {main_dish} with {side}."

@my_greet_func
def lol():
    """Return lol"""
    return "lol"

print()
print(greet("Dread"))
print(order("beef", "pasta"))
print(lol())

print()
print(greet.__doc__)
print(greet.__name__)
help(greet)