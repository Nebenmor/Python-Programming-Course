guest_list = ['marginal', 'knox', 'caxxie', 'mishuzo']
print(f"Hello {guest_list[0].title()}, I would love to invite you for dinner")
print(f"Hello {guest_list[1].title()}, How's \"Bangladesh?\" I would love to invite you for dinner")
print(f"Hello {guest_list[2].capitalize()}, I would love to invite you for dinner")
print(f"Hello {guest_list[3].title()}, you are invited to dinner at my place")

print(f"\nAm sorry to announce that {guest_list[3].title()} won't be coming for the dinner")

guest_list[3] = 'TonyTenik'

print(f"\nHello {guest_list[0].title()}, I would love to invite you for dinner")
print(f"Hello {guest_list[1].title()}, I would love to invite you for dinner")
print(f"Hello {guest_list[2].capitalize()}, I would love to invite you for dinner")
print(f"Hello {guest_list[3]}, you are invited to dinner at my place")

print("\nHello everyone, I have good news. I found a bigger table so now we can invite more guests")

guest_list.insert(0, 'pryanayafreak')
guest_list.insert(2, 'nourek')
guest_list.append('Seven')

print(f"\nHello {guest_list[0].title()}, I would love to invite you for dinner")
print(f"Hello {guest_list[1].title()}, I would love to invite you for dinner")
print(f"Hello {guest_list[2].capitalize()}, I would love to invite you for dinner")
print(f"Hello {guest_list[3].title()}, you are invited to dinner at my place")
print(f"Hello {guest_list[4].title()}, you are invited to my dinner bash")
print(f"Hello {guest_list[5]}, you are invited to my dinner party")
print(f"Hello {guest_list[6].title()}, you are specially invited to my dinner night")

print(guest_list)

print("\nHello everyone, I have an announcement. Unfortunately I can only invite two people for dinner because the new dinner table won't arrive on time for dinner\n")

popping_1 = guest_list.pop()
print(f"Hello {popping_1.title()}, am sorry but I can't invite you to the dinner anymore")

popping_2 = guest_list.pop()
print(f"Hello {popping_2}, am sorry but I can't invite you to the dinner anymore")

popping_3 = guest_list.pop()
print(f"Hello {popping_3.title()}, am sorry but I can't invite you to the dinner anymore")

popping_4 = guest_list.pop()
print(f"Hello {popping_4.title()}, am sorry but I can't invite you to the dinner anymore")

popping_5 = guest_list.pop()
print(f"Hello {popping_5.title()}, am sorry but I can't invite you to the dinner anymore")

print(guest_list)

del guest_list [0]
del guest_list [0]

print(guest_list)
