cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:") 
print(cars)
print("\nHere is the reversed list:")
cars.reverse() 
print(cars)
print("\nHere is the sorted list:") 
#cars.sort()
print(sorted(cars))
print("\nHere is the reverse sorted list again:")
cars.sort(reverse=True) 
print(cars)
print("\nHere is the length of the list:") 
print(len(cars))
# cars[] is now sorted in reverse
# is no longer in original order
print(cars)
