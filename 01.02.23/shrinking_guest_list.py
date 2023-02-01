dinner_guests = ["Albert Einstein", "Steve Jobs", "Elon Musk"]

print("Hello " + dinner_guests[0] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[1] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[2] + ", I would like to invite you to dinner.")

print(dinner_guests[1] + " cannot make it to the dinner.")

dinner_guests[1] = "Bill Gates"

for dinner_guest in dinner_guests:
    print(f"Hi {dinner_guest}, you are invited to have dinner with us.")

print("I found a bigger dinner table!")

dinner_guests.insert(0, "Yuval Noah Harari")
dinner_guests.insert(int(len(dinner_guests)/2), "Larry Page")
dinner_guests.append("Sergey Brin")

for dinner_guest in dinner_guests:
    print(f"Hi {dinner_guest}, you are invited to have dinner with us.")

print("Unfortunately, we can only invite two people for dinner.")

while len(dinner_guests) > 2:
	sorry_guest = dinner_guests.pop()
	print("Sorry, " + sorry_guest + " you can't be invited to dinner.")

for dinner_guest in dinner_guests:
	print("You are still invited, " + dinner_guest)

del dinner_guests[:]
print(dinner_guests)