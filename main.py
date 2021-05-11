
  # My Python weather program to find current
  # weather details of any city
  # using openweathermap api

  #friendly greeting
print("Welcome to my super useful weather-checking program.")

  #required API stuff
  #importing request module
import requests
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
# My OpenWeatherMapAPI key
api_key = "a346e35af7ce4bdcdff5f710fe121aff"

#setting up loop for multiple tries
def main():
  user_search = input("To search by Zip Code, enter 'z'\nTo search by City name enter 'c'\n: ")

  #Give the user a choice to search by zip or city

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
    # "404", means zip code is found, elsewise
    # zip code is not found and user is notified
    if x["cod"] != "404":

      # store the value of "main" key in variable y
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

      # print following values in easy to read format
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

      print ("\nDo you want to try another location?")
      user_again = input("Enter 'y' or any key to exit: ")
      if user_again == 'y':
        main()
      else:
        print ("\nThank you for using my weather program!")
  
    else:
      print(" Zip Code Not Found ") #in case the user inputs bad zip
      main() #looping to beg

  elif user_search == "c":
    city_name = input("Enter US City name: ")

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
    # zip code is not found & user is notified
    if x["cod"] != "404":

      # store the value of "main" key in variable y
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

      # print following values in easy to read format
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
    
      print ("\nDo you want to try another location?")
      user_again = input("Enter 'y' or any key to exit: ")
      if user_again == 'y':
        main() #looping to beg
      else:
        print ("\nThank you for using my weather program!")

    else:
      print(" City Not Found ") #in case a mispelled city is given
      main() #looping to beg
  else:
    print("Wrong key!")
    main()  
main()

