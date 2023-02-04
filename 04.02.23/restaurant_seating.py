# Program to check if table is ready or not for dinner group
group_size = int(input("How many people are in your dinner group? "))

if group_size > 8:
	print("Sorry, you'll have to wait for a table.")
else:
	print("Your table is ready.")