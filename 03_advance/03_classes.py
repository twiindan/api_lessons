#-*- coding: utf-8 -*-
'''
MOD 11: Classes
'''


# Let's see how to declare custom classes


class Spam:       # 'class' keyword, camel case class name and colon :
    pass

spammer = Spam()  # Class instantiation: spammer becomes an instance of Spam

print(spammer)


# Easy, right?


class Eggs(Spam):                       # Ancestor superclasses inside parentheses for inheritance

    a_class_attr = "class_val"          # Class attributes inside the body, outside class methods. Must have value

    def __init__(self, attr_val):       # __init__ is called in the instances initialization (not constructor)
        self.attr = attr_val

    def method(self, arg1, arg2=None):  # Method declaration. Indented and receiving self (the instance)
        print("'method' of", self)
        print(self.attr, arg1, arg2)     # Access instance attributes using self with a dot .

    def second_method(self):
        self.attr = 99.99
        self.method("FROM 2nd")         # Methods may call other methods using self with a dot .


# Still easy?


egger = Eggs(12.345)                    # Provide __init__ arguments in the instantiation

print(egger)

print(egger.attr)                        # Retrieve instance attributes with a dot

print(egger.a_class_attr)                # Retrieve class attributes with a dot

print(Eggs.a_class_attr)

egger.a_class_attr = "new value"

print(egger.a_class_attr)
print(Eggs.a_class_attr)

#===============================================================================
# - Class attributes can be retrieved directly from the class
# - Instances only modify class attributes value locally
#===============================================================================


#===============================================================================
# - Classes are objects too:
#    - Python evaluates its declaration and instantiates a special object
#    - This object is called each time a new class instance is created
#===============================================================================


egger.method("value1", "value2")

egger.second_method()

inst_method = egger.method
inst_method("valueA", "valueB")


#===============================================================================
# - Methods are also attributes (bounded) of classes and instances
#===============================================================================


# Let's play a bit with inheritance


class Spam(object):
    spam_class_attr = "spam"                             # Class attributes must have value always (you may use None...)

    def spam_method(self):
        print("spam_method", self, self.spam_class_attr)
        print(self.__class__)


class Eggs(object):
    eggs_class_attr = "eggs"

    def eggs_method(self):
        print("eggs_method", self, self.eggs_class_attr)
        print(self.__class__)


class Fooo(Spam, Eggs):                                  # Specify a list of ancestor superclasses
    fooo_class_attr = "fooo"

    def fooo_method(self):
        self.spam_method()
        self.eggs_method()                               # Retrieve superclasses attributes as if they were yours
        print("fooo_method", self, self.fooo_class_attr)
        print(self.__class__)

foooer = Fooo()

foooer.fooo_method()

foooer.spam_method()

foooer.eggs_method()  # self is ALWAYS an instance of the subclass

print(foooer.spam_class_attr)
print(foooer.eggs_class_attr)
print(foooer.fooo_class_attr)  # We have access to all own and ancestors' attributes


# Given that Python is a dynamic language...

class Spam(object):
    pass

spammer = Spam()
spammer.name = "John"
spammer.surname = "Doe"
spammer.age = 65
spammer.male = True      # ... this is legal

print(spammer.name)
print(spammer.surname)
print(spammer.age)
print(spammer.male)



#===============================================================================
# REMEMBER:
#     - Classes are declared with the 'class' keyword, its name in camel case and a colon
#         - Specify ancestors superclasses list between parentheses after the class name
#         - So you must inherit ALWAYS from 'object' to have new-style classes
#     - Use indentation for class body declarations (attributes and methods)
#     - Specify class attributes (with value) inside the class, outside any method
#     - Specify methods inside the body, with indentation (method body has 2x indentation)
#         - Method's first parameter is always self, the instance whose method is being called
#         - Use self to access attributes and other methods of the instance
#     - When inheriting, ancestors attributes and methods can be accessed transparently
#     - There are no private attributes in Python
#         - There is a convention to use underscore _ prefix
#     - Classes definition is not closed. At any time you can add (or delete) an attribute
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/tutorial/classes.html#a-first-look-at-classes
#  - http://docs.python.org/2/library/functions.html#classmethod
#  - http://docs.python.org/2/library/functions.html#staticmethod
#  - http://docs.python.org/2/reference/compound_stmts.html#function
#  - http://docs.python.org/2/reference/datamodel.html#types (see Classes and Class instances)
#===============================================================================
