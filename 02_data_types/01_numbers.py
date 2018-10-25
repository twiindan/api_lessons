#-*- coding: utf-8 -*-



spam = 65              # an integer declaration.
print(spam)

print(type(spam))       # this is a function call

eggs = 2
print(eggs)
print(type(eggs))

# Let's see the numeric operations

print(spam + eggs)      # sum

print(spam - eggs)      # difference

print(spam * eggs)      # product

print(spam / eggs)      # quotient

print(spam % eggs)      # remainder or module

print(spam ** eggs)     # power

fooo = -2              # negative value
print(fooo)
print(type(fooo))

print(-fooo)            # negated

print(abs(fooo))        # absolute value

print(int(fooo))        # convert to integer

print(float(fooo))      # convert to float

fooo += 1              # auto incremental
print(fooo)

# More on the quotient

print(spam / eggs)          # quotient
print(spam / float(eggs))   # quotient

# More on the operations result type

print(type(spam + eggs))
print(type(float(spam) + eggs))

#===============================================================================
# - Python automatically infers the type of the result depending on operands type
#===============================================================================

# Let's try again the power

print(eggs ** spam)
print(type(eggs ** spam))


#===============================================================================
# - Use parentheses to alter operations order
#===============================================================================


#===============================================================================
# Python numeric types:
#  - int:
#     - Traditional integer
#     - Implemented using long in C, at least 32 bits precision
#     - Its values are [-sys.maxint - 1, sys.maxint]
#  - long:
#     - Long integer with unlimited precision
#     - Created automatically or when an L suffix is provided
#  - float:
#     - Floating point number
#     - Specified with a dot . as decimals separator
#     - Implemented using double in C
#     - Check sys.float_info for its internal representation
#
#===============================================================================


#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex
#===============================================================================
