countries = ['India', 'USA', 'China', 'Japan', 'Germany']

print('Original List:', countries)

# Use sorted() to print list in alphabetical order without changing original list
print('Alphabetical Order:', sorted(countries))

# Use len() to find the length of the list
print('Length of List:', len(countries))

# Use reverse() to reverse the order of the list
countries.reverse()
print('Reversed List:', countries)

# Use sort() to sort the list in alphabetical order
countries.sort()
print('Sorted List:', countries)

# Use append() to add a new element to the list
countries.append('Russia')
print('List after adding a new element:', countries)

# Use pop() to remove an element from the list
countries.pop()
print('List after popping an element:', countries)

# Use insert() to insert an element at a specific index
countries.insert(1, 'Mexico')
print('List after inserting an element:', countries)