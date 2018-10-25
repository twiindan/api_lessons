
# We can implement a LIFO (Last In First Out) Queue using the append and pop list methods.

stack = ["python", "selenium", "hello"]

# add an element to the end of the list
stack.append("new")
stack.append(6)
print (stack)

# retrieve the last item from list
element = stack.pop()
print(stack)
print(element)

# retrieve the last item from list
second_element = stack.pop()
print(stack)
print(second_element)

# add an element to the end of the list
stack.append("end")
print(stack)
