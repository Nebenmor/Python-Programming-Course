#Using the remove() method to delete elements from a list by their values

motorcycles = ['Ducati', 'Honda', 'Yamaha', 'Suzuki']
print(motorcycles)

too_expensive = 'Ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print(f"\nA {too_expensive.title()} is too expensive for me")