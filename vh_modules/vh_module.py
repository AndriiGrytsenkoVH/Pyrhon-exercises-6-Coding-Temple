from time import time

def time_this_func(func, iterations, *args):
    start = time()
    for _ in range(iterations):
        func(*args)
    end = time()
    print(f"{func}")
    print(end - start)

def print_init(string_of_things):
    """
    Prints out attributes for __init__ of a class using it's arguments
    """
    things = string_of_things.split(", ")
    for attribute in things:
        print(" "*8 + f"self.{attribute} = {attribute}")
        