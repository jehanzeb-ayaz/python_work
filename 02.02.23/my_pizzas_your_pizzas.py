pizzas = ["Pepperoni", "Margherita", "Hawaiian"]
friend_pizzas = pizzas[:]

pizzas.append("Veggie Delight")
friend_pizzas.append("Seafood Delight")

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)