# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'fighter fish',
    'name': 'romeo',
    'owner': 'ruwaiz',
    'weight': 10,
    'eats': 'fish food',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'cristiano',
    'owner': 'abdullah',
    'weight': 10,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'ronaldo',
    'owner': 'eric',
    'weight': 37,
    'eats': 'dog food',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))