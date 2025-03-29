import folium
import os
from frontend.py import  user_data
from geopy.geocoders import Nominatim
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time
from PIL import Image

def get_map_image(location):
    geolocator = Nominatim(user_agent="geo_locator")
    loc = geolocator.geocode(location)

    if not loc:
        print(" Location not found! Please enter a valid place.")
        return
    
    lat, lon = loc.latitude, loc.longitude
    print(f" Latitude: {lat}, Longitude: {lon}")

    my_map = folium.Map(location=[lat, lon], zoom_start=15, tiles="OpenStreetMap")
    folium.Marker([lat, lon], popup=f" {location}", tooltip="Click for details").add_to(my_map)

    map_file = "map.html"
    my_map.save(map_file)

    def start_server():
        httpd = HTTPServer(("localhost", 8000), SimpleHTTPRequestHandler)
        httpd.serve_forever()

    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    time.sleep(2)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--window-size=800x600")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get("http://localhost:8000/map.html")
    time.sleep(3)

    image_file = "map.png"
    return(image_file)
    driver.save_screenshot(image_file)
    driver.quit()

    #img = Image.open(image_file)
    #img.show()
    #print(f"✅ Map image saved as '{image_file}'")

# Example Usage
#location = input("Enter a location (e.g., New York, Eiffel Tower): ")
location=user_data[1]
#location="Chennai"
img=get_map_image(location)
file_path = os.path.abspath(img)
print(file_path)
