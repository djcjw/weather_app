#friendly greeting
print("Welcome to my super useful weather-checking app.\nYou will enter your zip code or city name to obtain weather forecast info.")

#set the name input variable
name = input("\nPlease enter in your name: ")

def greet_user():
  """Function to display a simple titled greeting using inputted name."""
  print(f"\nHello {name.title()}!")
greet_user()

#def user_info_request():
  #print("\nPlease enter your 5-digit zip code or city:")

zip = input('\nPlease enter your zip code:')
zip = int(zip)
if len(str(zip)) < 5 or len(str(zip)) > 5:
  print ("try again")
  
else:
  user_zip = zip
  print (user_zip)
  print (f"You entered a valid zip. Checking now: ")

    #return zip


def user_city():
  city = ''
  while city != '1' and city != '2':
    print('\nWhich cave will you go into? (1 or 2)')
    city = input()
  return city



#greet_user()
#user_zip1 = user_zip()


