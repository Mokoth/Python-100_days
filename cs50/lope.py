# name = ''
# while name != 'your name':
#     print('Please enter your name: ')
#     name = input()
# print('Thanks')


# with break

# while True:
#     print('Enter your name: ')
#     name = input()
#     if name == 'your name':
#         break
# print('Thanks')


# with a function 

# break

# def main():
#     # meow(3)
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         num = int(input('Enter a num: '))
#         if num > 0:
#             break
#     return num

# def meow(n):
#     for _ in range(n):
#         print('Meow')

# main()



# continue

# while True:
#     print('Type your name: ')
#     name = input()
#     if name != 'Joe':
#         continue
#     print('Hello, Joe, what\'s your password?')

#     print('Type your password: (its a fish)')
#     password = input()
#     if password == 'swordfish':
#         break
# print('Access granted!')

named = ''
while not named:
    print('Please type your name: ')
    named = input()
print('How man guests are you willing to have? ')
num_guests = int(input())
if num_guests:
    print('Be sure to have enough rooms for your guests!')
print('Done!')