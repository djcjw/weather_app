#friendly greeting
print("Welcome to my super useful weather-checking app.\nYou will enter your zip code or city name to obtain weather forecast info.")

import requests

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

#starting web REST API setup 


appid = "a346e35af7ce4bdcdff5f710fe121aff"

WS_URL = "api.openweathermap.org"

#http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_key}

#api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_Key}

#Hourly forecast by OpenWeatherMap! Hourly forecast for 4 days, with 96 timestamps and higher geographic accuracy.

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state code}&appid={API key}

##pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state code},{country code}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?id={city ID}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?id=524901&appid={API_Key}

'''
querystring = {"zip":"68144","APPID":"a346e35af7ce4bdcdff5f710fe121aff"} 

headers = { 'cache-control': "no-cache” }

response = requests.request("GET", WS_URL, headers=headers, params=querystring) 

print(response.text)
'''
#greet_user()
#user_zip1 = user_zip()



# change the following line to use your own API key


city = "London"

parameters = {'access_key': appid, 'query': city}

response = requests.get(WS_URL, parameters)
js = response.json()
print(js)
print()

temperature = js['current']['temperature']
date = js['location']['localtime']
city = js['location']['name']
country = js['location']['country']

print(f"The temperature in {city}, {country} on {date} is {temperature} degrees Celsius")
