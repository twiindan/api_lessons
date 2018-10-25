#-*- coding: utf-8 -*-


spam = "spam"                    # a string
print(spam)

print(type(spam))

eggs = 'eggs'                  # another string
print(eggs)
print(type(eggs))


#===============================================================================
# - Backslash \ is the escape character
#===============================================================================

scaped = 'I\'m learning Python!'
print(scaped)



spam_eggs = "'\tspam\n\teggs'"   # another string
print(spam_eggs)
print(type(spam_eggs))

# Let's continue with strings


spam_eggs = """'spam
eggs'"""                       # another string
print(spam_eggs)
print(type(spam_eggs))

#===============================================================================
# - Three single or double quotes also work, and they support multiline text
#===============================================================================

spam_eggs = "'\tspam" "\n\teggs'"  # another string
print(spam_eggs)
print(type(spam_eggs))

#===============================================================================
# - Several consecutive string literals are automatically concatenated, even if
#   declared in different consecutive lines
#    - Useful to declare too much long string literals
#===============================================================================

spam_eggs = u"'\tspam\n \
\teggs'"  # a unicode string
print(spam_eggs)
print(type(spam_eggs))

#===============================================================================
# - Backslash \ can even escape line breaks
#    - Useful to declare too much long string literals
#===============================================================================


# Let's see strings operations

spam = "spam"
eggs = u'"Eggs"'

num_str = str(2)                           # Convert integer into string
print(num_str)

print(spam.capitalize())                    # Return a copy with first character in upper case

print(spam)

print(spam.endswith("am") )                 # Check string suffix

print(eggs.startswith(("eggs", "huevos")))  # Check string prefix (optionally use a tuple)

print(spam.find("pa"))                      # Get index of substring (or -1)

print(eggs.upper())
print(eggs.lower())                         # Convert to upper or lower case

print(spam.isupper())
print(spam.islower())                       # Check if string is in upper or lower case

print(" | spam # ".strip())
print(" | spam # ".strip(' |#'))      # Remove leading and trailing characters (only whitespace by default)

print("spam, eggs, foo".split(", "))
print("spam, eggs, foo".split(", ", 1))     # Split by given character, returning a list (optionally specify times to split)

print(", ".join(("spam", "eggs", "foo")))   # Use string as separator to concatenate an iterable of strings

# Let's format strings

print("%s %s %d" % (spam, spam, 7))         # This is the old string formatting, similar to C

print("{0} {0} {1}".format(spam, 7))        # This is the new string formatting method, standard in Py3k

print("{} {}".format(spam, 7.12345))

# Change strings

print(spam[0])                            # Strings are lists and we can get the value by index
spam[0] = 'm'                             # Change one character of the string by index

# Is not possible change a character in a string because the strings are inmutable elements.
# To change it, you should create another string or convert to List

spam_list = list(spam)
spam_list[0] = 'm'
spam = ''.join(spam_list)
print(spam)




#===============================================================================
# SOURCES:
#  - http://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex
#  - http://docs.python.org/2/reference/lexical_analysis.html#strings
#  - http://docs.python.org/2/reference/lexical_analysis.html#encodings
#  - http://docs.python.org/2/library/stdtypes.html#string-methods
#  - http://docs.python.org/2/library/string.html#formatstrings
#===============================================================================

#==============================================================================
# TIME TO START WORKING:
#   - go to basic\exercises directory
#   - execute the mod_04_strings.py
#   - try to implement the functions indicated
#==============================================================================
