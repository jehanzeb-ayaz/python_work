places = ["Paris", "London", "Shanghai", "New York", "Bali"]

# Original order
print("Original order: ", places)

# Alphabetical order
print("Alphabetical order: ", sorted(places))

# Show original order
print("Original order: ", places)

# Reverse Alphabetical order
print("Reverse Alphabetical order: ", sorted(places, reverse=True))

# Show original order
print("Original order: ", places)

# Reversed order
places.reverse()
print("Reversed order: ", places)

#Reversed order again
places.reverse()
print("Original order: ", places)

#Alphabetical order
places.sort()
print("Alphabetical order: ", places)

#Reverse Alphabetical order
places.sort(reverse=True)
print("Reverse Alphabetical order: ", places)