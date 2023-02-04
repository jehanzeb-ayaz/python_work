"""
person = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}

print("First name:", person['first_name'])
print("Last name:", person['last_name'])
print("Age:", person['age'])
print("City:", person['city'])
"""
person1 = {'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'city': 'New York'}
person2 = {'first_name': 'Jane', 'last_name': 'Smith', 'age': 25, 'city': 'London'}
person3 = {'first_name': 'Bob', 'last_name': 'Johnson', 'age': 35, 'city': 'Paris'}

people = [person1, person2, person3]

for person in people:
    print("First name:", person['first_name'])
    print("Last name:", person['last_name'])
    print("Age:", person['age'])
    print("City:", person['city'])
    print("")