# Code for rivers and their countries
rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'yangtze': 'china'
}

# Sentence about each river
for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

# Name of each river
print("\nList of rivers:")
for river in rivers:
	print(river.title())

# Name of each country
print("\nList of countries:")
for country in rivers.values():
	print(country.title())