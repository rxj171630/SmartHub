import googlemaps
from datetime import datetime
import json

gmaps = googlemaps.Client(key='AIzaSyC2GcW4pAHJuyTJJnsm3fV-krl0nCpOokw')

# Geocoding an address
#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

# Look up an address with reverse geocoding
#reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

# Request directions via public transit
now = datetime.now()
to_dir = "University of Illinois"
from_dir = "University of Wisconsin"

dist_mat = gmaps.distance_matrix(origins=from_dir,destinations=to_dir,mode='driving',departure_time=now)
print(dist_mat)
