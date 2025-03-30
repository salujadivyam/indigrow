import requests
import time
from geopy.geocoders import Nominatim

# Get Latitude & Longitude from Location
def get_lat_lon(location):
    geolocator = Nominatim(user_agent="weather_app/1.0 (your_email@example.com)")
    time.sleep(1)  # Delay to prevent rate-limiting
    geo_location = geolocator.geocode(location)

    if geo_location:
        return geo_location.latitude, geo_location.longitude
    else:
        raise ValueError("Could not find location!")

# Get Weather Forecast from Open-Meteo API
def get_weather_forecast(lat, lon):
    url = f"https://api.open-meteo.com//v1//forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve weather data.")
        return None

# Calculate Rain Probability based on Precipitation
def calculate_rain_probability(precipitation):
    """Estimate rain probability based on precipitation values (mm)."""
    if precipitation == 0:
        return 0  # No precipitation → No chance of rain
    elif 0 < precipitation <= 0.5:
        return 20  # Low probability of rain
    elif 0.5 < precipitation <= 2:
        return 50  # Moderate probability
    elif 2 < precipitation <= 5:
        return 75  # High probability
    else:
        return 90  # Very high probability of rain

# Get Weather Description Based on Weather Code
def get_weather_description(code):
    """Maps Open-Meteo weather codes to descriptive conditions."""
    weather_descriptions = {
        0: "Clear Sky",
        1: "Mainly Clear",
        2: "Partly Cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Fog with Rime",
        51: "Drizzle (Light)",
        53: "Drizzle (Moderate)",
        55: "Drizzle (Dense)",
        61: "Rain (Slight)",
        63: "Rain (Moderate)",
        65: "Rain (Heavy)",
        71: "Snow (Slight)",
        73: "Snow (Moderate)",
        75: "Snow (Heavy)",
        95: "Thunderstorms (Slight/Moderate)",
        96: "Thunderstorms with Hail (Slight)",
        99: "Thunderstorms with Hail (Heavy)",
    }
    return weather_descriptions.get(code, "Unknown Weather")

# Get Weather Data and Rain Probability for Frontend
def get_weather_data_for_frontend(district):
    """Fetch weather and rain probability based on district name."""
    try:
        # Get coordinates of the district
        lat, lon = get_lat_lon(district)

        # Fetch weather forecast for the location
        data = get_weather_forecast(lat, lon)
        if data:
            # Get today's weather data
            max_temp = data['daily']['temperature_2m_max'][0]
            min_temp = data['daily']['temperature_2m_min'][0]
            precipitation = data['daily']['precipitation_sum'][0]
            wind_speed = data['daily']['windspeed_10m_max'][0]
            weather_code = data['daily']['weathercode'][0]

            # Get rain probability and weather condition
            rain_probability = calculate_rain_probability(precipitation)
            weather_condition = get_weather_description(weather_code)

            # Return data for frontend display
            return weather_condition,rain_probability,max_temp
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None