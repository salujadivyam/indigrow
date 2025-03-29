import requests
import matplotlib.pyplot as plt
#from PIL import Image
from io import BytesIO
from geopy.geocoders import Nominatim

# NASA GIBS Configuration
NASA_GIBS_URL = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi"
#LAYER = "MODIS_Terra_CorrectedReflectance_TrueColor"  # Satellite Layer
DATE = "2024-03-01"  # Change this if needed
#WIDTH, HEIGHT = 500, 500  # Image resolution

# Function to get latitude & longitude from location
def get_lat_lon(location):
    geolocator = Nominatim(user_agent="satellite_imagery_app")
    geo_location = geolocator.geocode(location)
    if geo_location:
        return geo_location.latitude, geo_location.longitude
    else:
        raise ValueError("Could not find location!")



# Main function
def main():
    location = input("Enter location (e.g., New York): ")
    
    try:
        lat, lon = get_lat_lon(location)
        return([lat,lon])
        

    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    coord=main()
    print(coord)
