import requests
from datetime import datetime
from config import API_KEY, CITIES
from database import insert_daily_summary, fetch_daily_summaries

def fetch_weather_data():
    """
    Fetches current weather data for each city from the OpenWeatherMap API
    and stores it in a dictionary.
    """
    url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = {}

    for city in CITIES:
        try:
            response = requests.get(url, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
            if response.status_code == 200:
                data = response.json()
                weather_data[city] = {
                    'temp': data['main']['temp'],
                    'max_temp': data['main']['temp_max'],
                    'min_temp': data['main']['temp_min'],
                    'weather_condition': data['weather'][0]['description'],
                    'date': datetime.fromtimestamp(data['dt']).date()
                }

                # Insert data into the database
                insert_daily_summary(
                    city=city,
                    date=weather_data[city]['date'],
                    avg_temp=weather_data[city]['temp'],
                    max_temp=weather_data[city]['max_temp'],
                    min_temp=weather_data[city]['min_temp'],
                    weather_condition=weather_data[city]['weather_condition']
                )
            else:
                print(f"Error fetching data for {city}: {response.status_code}")
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")

    if not weather_data:
        print("No weather data fetched.")
    return weather_data

def get_daily_summaries():
    """
    Fetches the daily summaries stored in the SQLite database.
    """
    return fetch_daily_summaries()















