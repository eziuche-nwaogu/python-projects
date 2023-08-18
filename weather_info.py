# This gives the weather information about a particular location
import requests
import pprint

API_KEY = "7a43a74c7c7424851ad12ca59f4d0336"
location = input("Enter the location you wish to search for: ")
base_url = (
    "https://api.openweathermap.org/data/2.5/weather?q="
    + location
    + "&appid="
    + API_KEY
)
weather_data = requests.get(base_url).json()

lat_value = weather_data["coord"]["lat"]
humidity_value = weather_data["main"]["humidity"]
pressure_value = weather_data["main"]["pressure"]
temp_value = weather_data["main"]["temp"]
max_temp = weather_data["main"]["temp_max"]
min_temp = weather_data["main"]["temp_min"]
time_zone = weather_data["timezone"]
visibility_value = weather_data["visibility"]
wind_speed = weather_data["wind"]["speed"]
wind_angle = weather_data["wind"]["deg"]

print(f"The weather conditions for {location} are as follows:")
pprint.pprint(weather_data)  # Print the complete weather data if desired

print(f"The summary of the weather conditions of {location} is as follows:")
print(f"The latitude is {lat_value}")
print(f"The humidity is {humidity_value}%")
print(f"The pressure is {pressure_value}")
print(f"The temperature is {temp_value}K")
print(f"The maximum temperature is {max_temp}K")
print(f"The minimum temperature is {min_temp}K")
print(f"The time zone is {time_zone}")
print(f"The visibility is {visibility_value}")
print(f"The wind speed is {wind_speed}Km/h")
print(f"The wind angle is {wind_angle}degrees")
