prompt = "Please enter your age: "
age = int(input(prompt))

while age >= 0:
  if age < 3:
    price = 0
  elif age < 13:
    price = 10
  else:
    price = 15

  print("The cost of your movie ticket is $" + str(price) + ".")
  age = int(input(prompt))
