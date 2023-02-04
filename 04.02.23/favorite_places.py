favorite_places = {
	'John': ['Paris', 'London', 'Tokyo'],
	'Sarah': ['Rome', 'Barcelona'],
	'Michael': ['New York', 'Miami', 'San Francisco']
}

for name, places in favorite_places.items():
	print(f"{name}'s favorite places are:")
for place in places:
	print(f"- {place}")
	print("\n")