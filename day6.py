# Day 6 of 100 days: elif

print("SECURE LOGIN")
print()
username = input("Username > ")
password = input('Password >')

if username == 'mark' and password == 'password':
  print(f'Welcome {username}!')
elif username == 'Suzann' and password == 'Su74nne':
  print(f'Hey there {username}')
else:
  print('Go away!')

# Challenge 1
print()

season = input('what is your favorite season?')
if season == "spring":
  print("Ah! The birds are chirping and flowers blooming.")
elif season == 'summer':
  print("Catch some sun and cool off with a lemonade.")
elif season == 'autumn':
  print("The leaves are changing and the air is crisp. Enjoy!")
elif season == 'winter':
  print("Stay warm by the fire and watch the snow fall.")
else: 
  print("I don't know that season. Please try again.")