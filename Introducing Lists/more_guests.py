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