#-*- coding: utf-8 -*-


# Let's declare a function


def spam():       # Functions are declared with the 'def' keyword, its name, parentheses and a colon
    print("spam")  # Remember to use indentation!

spam()  # Functions are executed with its name followed by parentheses


# Let's declare a function with arguments


def eggs(arg1):         # Functions arguments are declared inside the parentheses
    print("eggs", arg1)

eggs("eggssss")  # Function calls specify arguments inside parentheses


def func(arg1, arg2, arg3):         # There is no limit of arguments
    print("func", arg1, arg2, arg3)

func("spam", "eggs", "fooo")


def my_sum(arg1, arg2):
    return arg1 + arg2    # Use the return keyword to output any result

print(my_sum(3, 5))


print(my_sum(3.333, 5))
print(my_sum("spam", "eggs"))  # Given that Python is a dynamic language we can reuse the same method


print(my_sum(arg2="spam", arg1="eggs"))  # Use keyword arguments to call arguments in different order



# Let's declare a function with arguments and default values


def my_pow(arg1, arg2=2):  # It is possible to define deault values for the arguments, always after arguments without default values
    return arg1 ** arg2

print(my_pow(3))


def my_func(arg1, arg2=2, arg3=3, arg4=4):
    return arg1 ** arg2 + arg3 ** arg4

print(my_func(3, arg3=2))  # Use keyword arguments to call skip some of the arguments with default value


def my_func(arg1=1, arg2=2, *args):  # This arbitrary list is a (kind-off) tuple of positional arguments
    print(args)
    return arg1 + arg2

my_func(2, 3)

my_func(2, 3, 5, 7)


# The same applies for arbitrary keyword arguments


def my_func(arg1=1, arg2=2, **kwargs):  # This arbitrary 'args' list is a (kind-off) tuple of positional arguments
    print(kwargs)
    return arg1 + arg2

my_func(2, 3)

my_func(2, 3, param3=5, param4=7)



#===============================================================================
# REMEMBER:
#     - Functions are declared with the 'def' keyword, its name, parentheses and a colon
#         - Specify arguments inside the parentheses
#         - Define arguments' default values with an equal, after arguments without def val
#         - Specify arbitrary arguments or keyword arguments with *args or **kwargs
#            - Actually only the asterisks matter, the name is up to you
#     - Use indentation for the body of the function, typically 4 spaces per level
#     - Functions are executed with its name followed by parentheses
#         - Provide input arguments inside the parentheses
#         - Provide keywords arguments specifying their name
#     - Functions can be declared and called outside classes
#     - Functions are first classed objects
#         - You can pass them as arguments
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/controlflow.html#defining-functions
#  - http://docs.python.org/2/tutorial/controlflow.html#more-on-defining-functions
#  - http://docs.python.org/2/reference/compound_stmts.html#function
#===============================================================================
