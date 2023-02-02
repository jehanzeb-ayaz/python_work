# Define the initial tuple of foods offered by the restaurant
foods = ('pizza', 'pasta', 'salad', 'sushi', 'tacos')

# Print each food using a for loop
print("Original menu:")
for food in foods:
	print(food)

# Try to modify one of the items
# This will raise an error, because tuples are immutable
try:
	foods[0] = 'lasagna'
except TypeError as e:
	print("\nError: " + str(e))

# Revise the menu by replacing two items
foods = ('lasagna', 'steak', 'salad', 'ramen', 'burrito')

# Print each food in the revised menu using a for loop
print("\nRevised menu:")
for food in foods:
	print(food)