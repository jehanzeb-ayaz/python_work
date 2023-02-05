sandwich_orders = ['tuna', 'chicken', 'veggie', 'ham and cheese']
finished_sandwiches = []

while sandwich_orders:
	current_order = sandwich_orders.pop()
	print(f"I made your {current_order} sandwich.")
	finished_sandwiches.append(current_order)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)