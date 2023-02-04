favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob']

for person in people_to_poll:
	if person in favorite_languages.keys():
		print(f"Thank you, {person.title()}, for taking the poll.")
	else:
		print(f"{person.title()}, please take the poll.")