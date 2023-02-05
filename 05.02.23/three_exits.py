# Using conditional test in the while statement
topping = ""
while topping != "quit":
	topping = input("Enter a topping you would like to add to your pizza (or 'quit' to stop): ").lower()
	if topping == "quit":
		break
	print(f"Adding {topping} to your pizza...")
	
	print("Thank you for your order!")

# Using an active variable to control how long the loop runs
active = True
while active:
	topping = input("Enter a topping you would like to add to your pizza (or 'quit' to stop): ").lower()
	if topping == "quit":
		active = False
	else:
		print(f"Adding {topping} to your pizza...")
	
	print("Thank you for your order!")

# Using a break statement to exit the loop when the user enters a 'quit' value
while True:
	topping = input("Enter a topping you would like to add to your pizza (or 'quit' to stop): ").lower()
	if topping == "quit":
		break
	print(f"Adding {topping} to your pizza...")

	print("Thank you for your order!")