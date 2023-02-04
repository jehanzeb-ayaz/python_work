pets = [
	{'kind': 'dog', 'owner': 'John'},
	{'kind': 'cat', 'owner': 'Sarah'},
	{'kind': 'fish', 'owner': 'Phil'},
	{'kind': 'bird', 'owner': 'Edward'},
	{'kind': 'hamster', 'owner': 'Jen'}
]

for pet in pets:
	print("The", pet['kind'], "belongs to", pet['owner'] + ".")