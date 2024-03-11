#Using the pop method to remove the last element of a list
motorcycles = []    #An empty list
motorcycles.append('honda') #honda is added to the  last position of the list
motorcycles.append('suzuki') #suzuki is added to the  last position of the list
motorcycles.append('yamaha') #yamaha is added to the  last position of the list
motorcycles.insert(0, 'ducati') #ducati is added to the first position of the list
print(motorcycles[0])   #All elememts of the list (motorcycles) are printed
print(motorcycles[1])
print(motorcycles[2])
print(motorcycles[3])

del motorcycles [3] #The del statement is used to delete the element at index position of 3, i.e yamaha
print(motorcycles)  #prints the current list of motorcycles

print(motorcycles.pop())  #print the element removed from the list by the pop() method, which is always the last element of the list and in this case, suzuki
print(motorcycles) #prints the current list of motorcycles after the pop() method has been used

pop_motorcycles = motorcycles.pop() #pops the last value of motorcycle and passes it to pop_motorcycles
print(f"The latest motorcycle I bought is {pop_motorcycles.upper()}")   #Using the pop() method to make a statement concerning the latest element or value of a list
print(motorcycles)  #prints the current list of motorcycles
print(f"The nicest motorcycle I bought is {pop_motorcycles.upper()}") #By passing the value returned by the pop() method to a variable, the same value can be called subsequently through the variable without executing the pop() method all over again
print(motorcycles)