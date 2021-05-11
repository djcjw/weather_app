
  # My Python weather program to find current
  # weather details of any city
  # using openweathermap api

  #friendly greeting
print("Welcome to my super useful weather-checking app.")

  #required stuff
  #inporting requuest module
import requests
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# My API key
api_key = "a346e35af7ce4bdcdff5f710fe121aff"

  #user input variables & functions
  #set the name input variable
#name = input("\nPlease enter in your name: ")
#def greet_user():
    #Function to display a simple titled greeting using inputted name.
    #print(f"\nHello {name.title()}!")
    #greet_user()

#setting up loop 
#def main():
user_search = input("To search by Zip Code, enter 'z'.\nTo search by City name enter 'c':\n ")

#determine if user_input is a City or a Zip

if user_search == "z":
  zip_code = input("Enter Zip Code: ")

# complete url address for zip lookup
  complete_url_zip = base_url + "zip=" + str(zip_code) + "&appid=" + api_key + "&units=imperial"
  response_c = requests.get(complete_url_zip)

  # get method of requests module
  # return response object

  # json method of response object
  # convert json format data into
  # python format data
  x = response_c.json()

  # Now x contains list of nested dictionaries
  # Check the value of "cod" key is equal to
  # "404", means zip code is found otherwise,
  # zip code is not found
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

    # store the value corresponding
    # to the "temp_min" key of y
    low_temp = y["temp_min"]

    # store the value corresponding
    # to the "temp_max" key of y
    high_temp = y["temp_max"]

    # store the value corresponding
    # to the "feels_like" key of y
    feels_like = y["feels_like"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature Forecast (Deg in Fahrenheit) = " +
          str(current_temperature) +
        "\n Low temp = " +
          str(low_temp) +
        "\n High temp = " +
          str(high_temp) +
        "\n Feels like = " +
          str(feels_like) +
        "\n Atmospheric Pressure (in hPa unit) = " +
          str(current_pressure) +
        "\n Humidity (in percentage) = " +
          str(current_humidiy) +
        "\n Description = " +
          str(weather_description))
  else:
    print(" Zip Code Not Found ")

elif user_search == "c":
  city_name = input("Enter US City name: ")

#starting web REST API setup
# complete url address for city lookup
  complete_url_city = base_url + "appid=" + api_key + "&q=" + city_name + "&units=imperial"
  response_c = requests.get(complete_url_city)

  # get method of requests module
  # return response object
  # json method of response object
  # convert json format data into
  # python format data
  x = response_c.json()

  # Now x contains list of nested dictionaries
  # Check the value of "cod" key is equal to
  # "404", means zip code is found otherwise,
  # zip code is not found
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

    # store the value corresponding
    # to the "temp_min" key of y
    low_temp = y["temp_min"]

    # store the value corresponding
    # to the "temp_max" key of y
    high_temp = y["temp_max"]

    # store the value corresponding
    # to the "feels_like" key of y
    feels_like = y["feels_like"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature Forecast (Deg in Fahrenheit) = " +
          str(current_temperature) +
        "\n Low temp = " +
          str(low_temp) +
        "\n High temp = " +
          str(high_temp) +
        "\n Feels like = " +
          str(feels_like) +
        "\n Atmospheric Pressure (in hPa unit) = " +
          str(current_pressure) +
        "\n Humidity (in percentage) = " +
          str(current_humidiy) +
        "\n Description = " +
          str(weather_description))
   
  else:
    print(" City Not Found ")

#print ("\nDo you want to try another location?")
#user_again = input("Enter 'y' or any key to exit: ")
#if user_again == 'y':
  #main()
#else:
  #print ("\nThank you for using my program!")
#main()

