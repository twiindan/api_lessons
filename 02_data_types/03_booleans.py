#-*- coding: utf-8 -*-
'''
MOD 07: Booleans
'''

# Let's declare some bools

spam = True
print(spam)

print(type(spam))


eggs = False
print(eggs)

print(type(eggs))


#===============================================================================
# Python truth value testing
#  - Any object can be tested for truth value
#  - Truth value testing is used in flow control or in Boolean operations
#  - All objects are evaluated as True except:
#     - None (aka. null)
#     - False
#     - Zero of any numeric type: 0, 0L, 0.0, 0j, 0x0, 00
#     - Any empty sequence or mapping: '', [], (), {}

#===============================================================================


# Let's try boolean operations

print(True or True)
print(True or False)
print(False or True)   # Boolean or. Short-circuited, so it only evaluates the second argument if the first one is False

print(True and True)
print(True and False)
print(False and True)  # Boolean or. Short-circuited, so it only evaluates the second argument if the first one is True

print(not True)
print(not False)


# What about comparisons?

spam = 2
eggs = 2.5

print(spam == 2)         # equal

print(spam != eggs)      # not equal

print(spam >= eggs)      # greater than or equal

print(spam > eggs)       # strictly greater than

print(spam <= eggs)      # less than or equal

print(spam < eggs)       # strictly less than

print(spam is 2)         # object identity, useful to compare with None (discussed latter)

print(spam is not None)  # negated object identity



#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/stdtypes.html#boolean-operations-and-or-not
#===============================================================================
