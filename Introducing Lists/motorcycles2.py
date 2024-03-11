#Using the pop() method to remove elements from any position of a list by using its index
motorcycles = ['Ducanti', 'Honda', 'Yamaha', 'Suzuki']

motorcycles.pop(0)  #The list was popped to specifically remove the element with an index of zero, i.e the first element

print(motorcycles)

print(f"The first motorcycle I ever bought was {motorcycles.pop(-1).upper()}")

popped_motorcycles_indexing = motorcycles.pop(0)

print(f"The best motorcycle I ever bought is {popped_motorcycles_indexing.upper()}")
print(motorcycles)