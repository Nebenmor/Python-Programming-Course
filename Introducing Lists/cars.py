#Note: The sort method sorts values permanently. The original order can no longer be accessed
cars = ['bmw', 'audi', 'toyota', 'subaru' ]
cars.sort() #The sort method sort values of a list alphabeticallu
print(cars)
cars.sort(reverse=True) #sort values in reverse alphabetic order
print(cars)

print(f"{cars[1].upper()}")