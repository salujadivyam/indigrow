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
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max,weathercode&timezone=auto"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve weather data")
        return None

# Calculate Rain Probability based on Precipitation
def calculate_rain_probability(precipitation):
    """
    Estimate rain probability based on precipitation values (mm).
    """
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
    """
    Maps Open-Meteo weather codes to descriptive conditions.
    """
    weather_descriptions = {
        0: "☀ Clear Sky",
        1: "🌤 Mainly Clear",
        2: "⛅ Partly Cloudy",
        3: "☁ Overcast",
        45: "🌫 Foggy",
        48: "🌫 Fog with Rime",
        51: "🌧 Drizzle (Light)",
        53: "🌧 Drizzle (Moderate)",
        55: "🌧 Drizzle (Dense)",
        61: "🌦 Rain (Slight)",
        63: "🌧 Rain (Moderate)",
        65: "🌧 Rain (Heavy)",
        71: "❄ Snow (Slight)",
        73: "❄ Snow (Moderate)",
        75: "❄ Snow (Heavy)",
        95: "⛈ Thunderstorms (Slight/Moderate)",
        96: "⛈ Thunderstorms with Hail (Slight)",
        99: "⛈ Thunderstorms with Hail (Heavy)",
    }
    return weather_descriptions.get(code, "🌥 Unknown Weather")

# Print the Weather Forecast
def print_weather_forecast(data):
    if data:
        print("\n📅 7-Day Weather Forecast:\n")
        
        # Iterate over daily forecast data
        for i, time in enumerate(data['daily']['time']):
            max_temp = data['daily']['temperature_2m_max'][i]
            min_temp = data['daily']['temperature_2m_min'][i]
            precipitation = data['daily']['precipitation_sum'][i]
            wind_speed = data['daily']['windspeed_10m_max'][i]
            weather_code = data['daily']['weathercode'][i]
            
            # Calculate rain probability
            rain_probability = calculate_rain_probability(precipitation)
            
            # Get weather description from weather code
            weather_condition = get_weather_description(weather_code)

            print(f"📆 Date: {time}")
            print(f"🌡 Max Temp: {max_temp}°C | Min Temp: {min_temp}°C")
            print(f"☔ Precipitation: {precipitation} mm")
            print(f"💨 Max Wind Speed: {wind_speed} km/h")
            print(f"🌧 Rain Probability: {rain_probability}%")
            print(f"🌥 Weather Condition: {weather_condition}\n")
    else:
        print("No weather data available")

# Main function to get input and display forecast
def main():
    location = input("🌍 Enter location (e.g., New York, USA): ")
    
    try:
        # Get coordinates of the location
        lat, lon = get_lat_lon(location)
        print(f"\n📍 Coordinates for {location}: Latitude = {lat}, Longitude = {lon}")

        # Get weather forecast
        weather_data = get_weather_forecast(lat, lon)

        # Print weather forecast
        print_weather_forecast(weather_data)
    
    except Exception as e:
        print(f"❗ Error: {e}")

# Run the application
if __name__ == "_main_":
    main()