import requests

api_key = ''# <-- Put your OpenWeatherMap appid here!

user_input = input("Enter Your City Name: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key})")

print(weather_data.status_code)

output = f'''

Today is {weather_data} in {user_input}

'''
print(output)
