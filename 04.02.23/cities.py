cities = {
	'Paris': {
	'country': 'France',
	'population': '2.148 million',
	'fact': 'It is known for its iconic Eiffel Tower and the Louvre Museum.'
	},
	'New York': {
	'country': 'United States',
	'population': '8.336 million',
	'fact': 'It is a global hub for finance, culture, and entertainment.'
	},
	'London': {
	'country': 'United Kingdom',
	'population': '8.9 million',
	'fact': 'It is home to the Buckingham Palace and the London Eye.'
	},
}

for city, info in cities.items():
	print(f"\nCity: {city}")
	country = info['country']
	population = info['population']
	fact = info['fact']
	print(f"\tCountry: {country}")
	print(f"\tPopulation: {population}")
	print(f"\tFact: {fact}")