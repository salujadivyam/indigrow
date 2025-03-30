import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Access the API keys
geomapts_api_key = os.getenv("GEOAPIFY_API_KEY")
import requests
from PIL import Image
from io import BytesIO

def get_lat_lon(location, api_key):
    url = f"https://api.geoapify.com/v1/geocode/search?text={location}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['features']:
            lat = data['features'][0]['geometry']['coordinates'][1]
            lon = data['features'][0]['geometry']['coordinates'][0]
            return lat, lon
        else:
            raise ValueError("Could not find location!")
    else:
        raise Exception(f"Failed to fetch latitude and longitude. HTTP Status Code: {response.status_code}")

def get_satellite_image(lat, lon, zoom=15, size="600x600", api_key="YOUR_GOOGLE_API_KEY"):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size={size}&maptype=satellite&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        return image
    else:
        raise Exception(f"Failed to fetch satellite image. HTTP Status Code: {response.status_code}")

if __name__ == "_main_":
    location = "Jaipur"
    GEOAPIFY_API_KEY = geomapts_api_key
    GOOGLE_API_KEY = ""
    
    try:
        lat, lon = get_lat_lon(location, GEOAPIFY_API_KEY)
        print(f"Latitude: {lat}, Longitude: {lon}")
        
        try:
            satellite_image = get_satellite_image(lat, lon, zoom=16, api_key=GOOGLE_API_KEY)
            satellite_image.show()
            satellite_image.save("satellite_image.png")
            print("Satellite image saved as 'satellite_image.png'.")
        except Exception as e:
            print(f"Error fetching satellite image: {e}")
    
    except Exception as e:
        print(f"Error fetching latitude and longitude: {e}")