import requests
import argparse

def get_argument():
    "return argument"
    parser = argparse.ArgumentParser(description="weather")
    parser.add_argument('-c','--city',required = True,help='city')
    parser.add_argument('-t''--temperature',help='temperature')
    parser.add_argument('-w','--wind',help='wind')
    args = parser.parse_args()
    return args.city,args.t__temperature,args.wind

def get_weather(city_name, option=None,option1=None):
    "print weather"
    api_key = 'fd4cb1d2df461f93214bb13aa66218bc'  # Replace with your actual API key
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric',  # Celsius
        'lang': 'en',  # Language
        'cnt':'12'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print("Weather information for", city_name)
        print("Temperature:", weather_data['main']['temp'], "°C")
        print("Weather:", weather_data['weather'][0]['description'])
        print("Humidity:", weather_data['main']['humidity'], "%")
        print("Pressure:", weather_data['main']['pressure'], "hPa")
        if option:
            if option.lower() == 'temperature':
                print("Feels like:", weather_data['main']['feels_like'], "°C")
            elif option1.lower() == 'wind':
                print("Wind:", weather_data['wind']['speed'], "meters")
            else:
                print("Invalid option. Available options: temperature, wind")
    else:
        print("Failed to retrieve weather data for", city_name)
        print("Error:", response.status_code)

if __name__ == "__main__":
    print('input temperature or wind the data')
    city,temp,speed = get_argument()
    get_weather(city,temp,speed)

