favorite_languages = {
	'jen': {'languages': ['python', 'ruby'], 'years': 8},
	'sarah': {'languages': ['c'], 'years': 5},
	'edward': {'languages': ['ruby', 'go'], 'years': 3},
	'phil': {'languages': ['python', 'haskell'], 'years': 10},
}

for name, info in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages and experience:")
	for key, value in info.items():
		if key == 'languages':
			print(f"\tLanguages: {', '.join(value)}")
		else:
			print(f"\tYears of experience: {value}")
