topping = ""
while topping != "quit":
    topping = input("Enter a topping you would like to add to your pizza (or 'quit' to stop): ").lower()
    if topping != "quit":
        print(f"Adding {topping} to your pizza...")
print("Thank you for your order!")
