# Day 3 of 100 days: Concatenate
# Combine strings and variables => using comma/+

print("=== Your Song Generator ===")
print("""You'll be asked a bunch of questions
then we'll make you up an amazing
song, totally copyright free 😭""")
print()
person = input("Name a person famous for something good: ")
thing = input("Name a thing they did: ")
place = input("Name a place you like: ")
rhyme = input("Give me a verb that rhymes with your person's name: ")
print()
print("There was a person called", person)
print("Who did something cool like", thing, "at the wonderful", place, "where you'll find me", rhyme)

# Challenge
food = input("Name a type of food: ")
plant = input("Name a plant: ")
cookingType = input("What is a way to cook something?")
burntFood = input("How do you describe burnt food?")
householdItem = input("Name something in your house: ")

print()
print("Tonight's dinner:")

print("For dinner you should make", cookingType, food, "with", burntFood, plant, "on a plate of", householdItem)