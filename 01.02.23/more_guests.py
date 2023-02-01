dinner_guests = ["Albert Einstein", "Steve Jobs", "Elon Musk"]

print("Hello " + dinner_guests[0] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[1] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[2] + ", I would like to invite you to dinner.")

print(dinner_guests[1] + " cannot make it to the dinner.")

dinner_guests[1] = "Bill Gates"

print("Hello " + dinner_guests[0] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[1] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[2] + ", I would like to invite you to dinner.")

print("I found a bigger dinner table!")

dinner_guests.insert(0, "Yuval Noah Harari")
dinner_guests.insert(int(len(dinner_guests)/2), "Larry Page")
dinner_guests.append("Sergey Brin")

print("Hello " + dinner_guests[0] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[1] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[2] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[3] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[4] + ", I would like to invite you to dinner.")
print("Hello " + dinner_guests[5] + ", I would like to invite you to dinner.")
