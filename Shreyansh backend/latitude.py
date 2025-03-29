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

# Function to fetch NASA satellite image
#def get_nasa_satellite_image(lat, lon):
    ##params = {
        #"SERVICE": "WMS",
        #"VERSION": "1.3.0",
        #"REQUEST": "GetMap",
        #"FORMAT": "image/png",
        #"LAYERS": LAYER,
        #"WIDTH": WIDTH,
        #"HEIGHT": HEIGHT,
        #"BBOX": bbox,
        #"CRS": "EPSG:4326",
        #"TIME": DATE
    #}
    
    #response = requests.get(NASA_GIBS_URL, params=params)

    #if response.status_code == 200:
        #image = Image.open(BytesIO(response.content))
        #return image
    #else:
        #raise ValueError(f"Failed to fetch image. Status Code: {response.status_code}")

# Main function
def main():
    location = input("Enter location (e.g., New York): ")
    
    try:
        lat, lon = get_lat_lon(location)
        return([lat,lon])
        
        #image = get_nasa_satellite_image(lat, lon)
        
        # Display the image
        #plt.imshow(image)
        #plt.axis("off")  # Hide axes
        #plt.title(f"Satellite Image of {location}")
        #plt.show()
    
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    coord=main()
    print(coord)
