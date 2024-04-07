import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

number = "00000000"  # Replace this with the phone number you want to track
pepnumber = phonenumbers.parse(number, "IN")  # Specify the country code as "IN"
location = geocoder.description_for_number(pepnumber, "en")
print("Location:", location)

service_pro = phonenumbers.parse(number, "IN")  # Specify the country code as "IN"
print("Service Provider:", carrier.name_for_number(service_pro, "en"))

KEY = 'OpencageApi'
geocoder = OpenCageGeocode(KEY)

# Include additional details such as city, region, and country for better accuracy
query = f"{location}, India"
results = geocoder.geocode(query)
print("OpenCage Results:", results)

# Ensure to select the first result for accuracy
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Latitude:", lat, "Longitude:", lng)

# Create a map and add a marker for the location
myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

# Save the map as HTML file
myMap.save("mylocation.html")
