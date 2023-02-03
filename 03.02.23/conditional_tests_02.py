# Tests for equality and inequality with strings
word = "hello"
print("Is word == 'hello'? I predict True.")
print(word == 'hello')

print("\nIs word == 'Hi'? I predict False.")
print(word == 'Hi')

# Tests using the lower() method
word = "Hello"
print("\nIs word.lower() == 'hello'? I predict True.")
print(word.lower() == 'hello')

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
num = 10
print("\nIs num == 10? I predict True.")
print(num == 10)

print("\nIs num != 10? I predict False.")
print(num != 10)

print("\nIs num > 5? I predict True.")
print(num > 5)

print("\nIs num >= 10? I predict True.")
print(num >= 10)

print("\nIs num < 15? I predict True.")
print(num < 15)

print("\nIs num <= 5? I predict False.")
print(num <= 5)

# Tests using the and keyword and the or keyword
num = 10
print("\nIs num > 5 and num < 15? I predict True.")
print(num > 5 and num < 15)

print("\nIs num > 15 or num < 5? I predict False.")
print(num > 15 or num < 5)

# Test whether an item is in a list
foods = ["pizza", "falafel", "carrot cake"]
print("\nIs 'pizza' in foods? I predict True.")
print('pizza' in foods)

# Test whether an item is not in a list
print("\nIs 'cannoli' not in foods? I predict True.")
print('cannoli' not in foods)