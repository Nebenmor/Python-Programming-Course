#Using splicing with lists
bicycles = ['Trek', 'cannondale', 'redline', 'specialized']
message = f"My favourite bicycle is a {bicycles[-2].title().removesuffix("line")}"

print(message)