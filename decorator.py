# Decorator

# a decorator is a design pattern that allows you
# to modify the functionality of a function by wrapping it in another function.

# The outer function is called the decorator,
# which takes the original function as an argument and returns a modified version of it.

# Basic implementation
def make_pretty(func):
    # define the inner function
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()

    # return the inner function
    return inner


# define ordinary function
def ordinary():
    print("I am ordinary")


# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()


# Decorating Functions with Parameters
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a / b)


divide(2, 5)
divide(2, 0)


# Chaining Decorators
# The order in which we chain decorators matter.
def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


@star
@percent
def printer1(msg):
    print(msg)
# printer1 = star(percent(printer1))


@percent
@star
def printer2(msg):
    print(msg)
# printer2 = percent(star(printer2))


printer1("Hello")
printer2("Bye")
