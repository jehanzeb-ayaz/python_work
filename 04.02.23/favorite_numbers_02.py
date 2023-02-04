favorite_numbers = {
    'John': [7, 10, 15],
    'Jane': [3, 4, 1],
    'Jim': [9, 12, 7],
    'Jessica': [11, 14, 19],
    'Josh': [5, 8, 2]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")