# Day 4 of 100 days: Print color
# Day 4 challenge: story line 
# f-string for literal string interpolation = only use ' '
# Print color using ("\033[31m hello, mom \33")

# Normalize using print(sep='', end=' ')

print("Welcome to your adventure simulator.")

print()
print("I am going to ask you a bunch of questions and then create an epic story with you as the star!")

print()
my_name = input("What is your name?: ")
print()
enemy_name = input("What is your worst enemy’s name?: ")
print()
superpower = input("What is your superpower?: ")
print()
location = input("Where do you live?: ")
print()
food = input("What is your favorite food?: ")

print()

print(f'Hello {my_name}! \033[31mYour ability\33[0m to {superpower} will make sure you never have to look at {enemy_name} again. Go eat {food} as you walk down the streets of \033[32m{location}\33[0m and use {superpower} for good and not evil!')
