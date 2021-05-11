# My Python program to find current
# weather details of any city
# using openweathermap api

#friendly greeting
print("Welcome to my super useful weather-checking app.")

#required stuff
#inporting requuest module
import requests
# My API key
api_key = "a346e35af7ce4bdcdff5f710fe121aff"
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#user input variables & functions
#set the name input variable
name = input("\nPlease enter in your name: ")
def greet_user():
  """Function to display a simple titled greeting using inputted name."""
  print(f"\nHello {name.title()}!")
greet_user()


user_search = input("Enter in a City Name or 5-digit Zip Code: ")

#determine if user_input is a City or a Zip

if user_search == int:
  print (f"You entered a valid zip. Checking now: ")
  user_search = zip
else:
  city_name = input()

#def user_info_request():
  #print("\nPlease enter your 5-digit zip code or city:")

#zip = input('\nPlease enter your zip code:')
#zip = int(zip)
#if len(str(zip)) < 5 or len(str(zip)) > 5:
  #print ("try again")
  
#else:
  #user_zip = zip
  #print (user_zip)
  #print (f"You entered a valid zip. Checking now: ")

    #return zip

#starting web REST API setup 





# Give city name


# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

	# store the value of "main"
	# key in variable y
	y = x["main"]

	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]

	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	current_humidiy = y["humidity"]

	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]

	# print following values
	print(" Temperature (in kelvin unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))

else:
	print(" City Not Found ")




#http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_key}

#api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_Key}

#Hourly forecast by OpenWeatherMap! Hourly forecast for 4 days, with 96 timestamps and higher geographic accuracy.

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state code}&appid={API key}

##pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state code},{country code}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?id={city ID}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?id=524901&appid={API_Key}
