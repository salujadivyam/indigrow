import requests
from geopy.geocoders import Nominatim
from datetime import datetime
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

def get_lat_long(location):
    """Convert location name to latitude and longitude."""
    geolocator = Nominatim(user_agent="nasa_gibs_fetcher")
    loc = geolocator.geocode(location)
    if loc:
        return loc.latitude, loc.longitude
    else:
        return None

def get_nasa_satellite_image(location):
    """Fetch and display the NASA GIBS satellite image for the given location."""
    lat_lng = get_lat_long(location)
    if not lat_lng:
        print("Location not found!")
        return
    
    lat, lon = lat_lng
    date = "2024-03-15"
    #date = datetime.today().strftime('%Y-%m-%d')  # Today's date
    zoom_level = 8  # Adjust zoom level (higher = more detail)

    # NASA GIBS API URL (MODIS Corrected Reflectance)
    nasa_url = f"https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?service=WMS&request=GetMap&layers=MODIS_Terra_CorrectedReflectance_TrueColor&styles=&format=image/png&width=512&height=512&crs=EPSG:4326&bbox={lat-1},{lon-1},{lat+1},{lon+1}&time={date}"

    # Fetch image
    response = requests.get(nasa_url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        
        # Display image
        plt.figure(figsize=(6,6))
        plt.imshow(image)
        plt.axis("off")
        plt.title(f"Satellite Image of {location} on {date}")
        plt.show()
    else:
        print("Failed to fetch image:", response.status_code)

# Get user input
location_input = input("Enter a location: ")
get_nasa_satellite_image(location_input)

