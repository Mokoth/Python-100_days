# Day 7 of 100 days: Nesting

tvShow = input("What is your favorite tv show?: ")
if tvShow == 'Pep show':
  print("Ugh, why")
  faveCharacter = input("Who is your favorite character?: ")
  if faveCharacter == 'Dias':
    print("Right answer")
  else:
    print("Nah, Dias show is the greatest!")
elif tvShow == "Paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all...")


# Challenge 2
print()
order = input("What would you like to order: Pizza or hamburger?")
if order == 'hamburger':
  print("Thank you!")
  cheese = input("Do you want cheese?")
  if cheese == 'yes':
    print("You got it.")
  else:
    print("No cheese it is!")
elif order == 'Pizza':
  print("Pizza coming in a short while...")
  topping = input("Do you want pepperoni on that? ")
  if topping == 'yes':
    print("We will add pepperoni")
  else:
    print("Your Pizza will not have pepperoni.")
else:
  print("No order made!")

# Challenge 3
# Fake Fan Question Generator
print ("Are you a fan of 'The Big Bang Theory' or a fake fan?")
print()
print("Answer these questions to find out.")

Glasses = input("Does someone wear glasses?")
if Glasses == "yes":
  print("Correct!")
else:
  print("Wrong!")
  WhoGlasses = input("And who wears glasses?")
  if WhoGlasses == "Leonard":
    print("You got it")
  else:
    print("Try again!")
  
