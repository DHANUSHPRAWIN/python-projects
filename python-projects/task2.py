import requests

def get_weather_and_sunrise_sunset(api_key, location):
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    sunrise_sunset_url = "https://api.sunrise-sunset.org/json"

    # Fetch weather data
    params_weather = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    response_weather = requests.get(weather_url, params=params_weather)

    # Fetch sunrise and sunset data
    params_sunrise_sunset = {
        "lat": "your_latitude_here",  # Replace with the actual latitude of the location
        "lng": "your_longitude_here",  # Replace with the actual longitude of the location
        "formatted": 0
    }
    response_sunrise_sunset = requests.get(sunrise_sunset_url, params=params_sunrise_sunset)

    if response_weather.status_code == 200 and response_sunrise_sunset.status_code == 200:
        data_weather = response_weather.json()
        temperature = data_weather['main']['temp']
        humidity = data_weather['main']['humidity']
        pressure = data_weather['main']['pressure']
        wind_speed = data_weather['wind']['speed']
        weather_description = data_weather['weather'][0]['description']

        data_sunrise_sunset = response_sunrise_sunset.json()
        sunrise = data_sunrise_sunset['results']['sunrise']
        sunset = data_sunrise_sunset['results']['sunset']

        print(f"Weather in {location}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Conditions: {weather_description}")
        print(f"Sunrise: {sunrise}")
        print(f"Sunset: {sunset}")
    else:
        print("Failed to fetch weather data or sunrise-sunset data.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY_HERE" #replace the API key of yours
    location = input("Enter city or ZIP code: ")
    get_weather_and_sunrise_sunset(api_key, location)
