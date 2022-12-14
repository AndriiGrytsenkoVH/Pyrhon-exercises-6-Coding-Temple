def print_init(string_of_things):
    """
    Prints out attributes for __init__ of a class using it's arguments
    """
    things = string_of_things.split(", ")
    for attribute in things:
        print(" "*8 + f"self.{attribute} = {attribute}")
        