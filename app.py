import requests

api_key = 'd3178a735d2906d912bf8572374c6495'
city = input("Enter City: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
print(weather_data.json())
if weather_data.json()['cod'] == '404':
    print("No city found")
else:

    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {city} is {weather} and {temp}")