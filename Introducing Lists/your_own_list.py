cars = ['Lamboghini', 'Venza', 'Benz', 'Honda']

print(f"I would love to own a \"{cars[0]}\" car someday, the Hurricane model") #The escape characters were used to escape the double quotation marks to ensure they are printed to stdI/O
print(f"{cars[-3]} is a popular brand of vehicle")

message = f"I plan to have a company that sells {cars[2]} cars"
print(message)

message = f"{cars[-1]} cars are one of the best in the world because of their durability"
print(message)

cars[0] = 'Ferrari'
print(f"I would love to own a \"{cars[0]}\" car someday.")
