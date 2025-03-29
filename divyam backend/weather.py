import requests
api_key = "7ae92b52aa3a4d5af6eccfbc1ec18cb2"
coord=[28.7041,77.1025]
lat = str(coord[0])
lon = str(coord[1])

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

response = requests.get(url)
data = response.json()

# Print the full response for debugging
print("API Response:", data)

if "list" in data:
    forecast = data["list"][0]  
    rain_chance = forecast.get("pop", 0) * 100  
    temperature = forecast["main"]["temp"]
    weather_desc = forecast["weather"][0]["description"]

    print(f"Weather at ({lat}, {lon}): {weather_desc}, {temperature}°C")
    print(f"Chance of Rain: {rain_chance}%")
else:
    print("Error: 'list' key not found in API response.")