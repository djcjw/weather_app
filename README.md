# weather_app
This is a useful weather-checking application

My API key:
a346e35af7ce4bdcdff5f710fe121aff

Requirements:

Create a Python Application which asks the user for their zip code or city. Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/ 

1. Display the weather forecast in a readable format to the user. 

2. Use comments within the application where appropriate in order to document what the program is doing. 

3. Use functions including a main function. 

4. Allow the user to run the program multiple times.

5. Validate whether the user entered valid data. If valid data isn’t presented notify the user. 

6. Use the Requests library in order to request data from the webservice. Use Python 3. 

7. Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.


#http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_key}

#api.openweathermap.org/data/2.5/forecast?id=524901&appid={API_Key}

#Hourly forecast by OpenWeatherMap! Hourly forecast for 4 days, with 96 timestamps and higher geographic accuracy.

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state code}&appid={API key}

##pro.openweathermap.org/data/2.5/forecast/hourly?q={city name},{state code},{country code}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?id={city ID}&appid={API key}

#pro.openweathermap.org/data/2.5/forecast/hourly?id=524901&appid={API_Key}