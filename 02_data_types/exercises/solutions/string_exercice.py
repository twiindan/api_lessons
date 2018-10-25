
python_string = "hello world"

# Capitalize the python_string variable but not using capitalize function. Find the index of "h" and "w" and change it
# to "H" and "W"

indexH = python_string.find("h")
indexW = python_string.find("w")

python_string_list = list(python_string)
python_string_list[indexH] = "H"
python_string_list[indexW] = "W"

python_string = "".join(python_string_list)

print(python_string)
