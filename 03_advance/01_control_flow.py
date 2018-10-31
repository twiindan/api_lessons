#-*- coding: utf-8 -*-
'''
MOD 08: Flow control
'''

# Let's start with the conditional execution

spam = [1, 2, 3]  # True
eggs = ""         # False

if spam:
    print("spam is True")
else:
    print("spam is False")

print("outside the conditional")  # Notice that there's is no closing fi statement


if spam:
    print("spam is True")
else:
    print("spam is False")

    print("still inside the conditional")


#==============================================================================
# REMEMBER:
# - Indentation is Python's way of grouping statements!!
#    - Typically four spaces per indentation level
#    - No curly brackets { } or semicolons ; used anywhere
#    - This enforces a more readable code
#==============================================================================


if eggs:
    print("eggs is True")
elif spam:
    print("eggs is False and spam is True")
else:
    print("eggs and spam are False")



spam = [1, 2, 3]  # True
eggs = ""         # False

print("first option" if spam else "second option")

print("first option" if eggs else "second option")




spam = [1, 2, 3]
while len(spam) > 0:
    print(spam.pop(0))

spam = [1, 2, 3]
idx = 0
while idx < len(spam):
    print(spam[idx])
    idx += 1


# What about the for loop?


spam = [1, 2, 3]
for item in spam:        # The for loop only iterates over the items of a sequence
    print(item)


eggs = "eggs"
for letter in eggs:      # It can loop over characters of a string
    print(letter)


spam = {"one": 1,
        "two": 2,
        "three": 3}
for key in spam:         # Or even it can iterate through a dictionary
    print(spam[key])      # Note that it iterates over the keys of the dictionary


# Let's see how to interact with loops iterations

spam = [1, 2, 3]
for item in spam:
    if item == 2:
        break
    print(item)

#===============================================================================
# - break statement halts a loop execution (inside while or for)
# - Only affects the closer inner (or smallest enclosing) loop
#===============================================================================
