# This program takes a person's name as input with leading and trailing whitespaces, 
# and displays the name after removing leading, trailing and leading and trailing whitespaces.

# Initialize the name variable with leading and trailing whitespaces
name = "\t\n Jehanzeb Ayaz \n\t"

# Display the name with leading and trailing whitespaces
print(name)

# Display the name after removing leading whitespaces
print(name.lstrip())

# Display the name after removing trailing whitespaces
print(name.rstrip())

# Display the name after removing leading and trailing whitespaces
print(name.strip())
