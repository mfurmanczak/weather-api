# importing geopy library
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
import time
from pprint import pprint

#initiate a new Nominatim client
app = Nominatim(user_agent="tutorial")

# get location raw data
location = app.geocode("Nairobi, Kenya").raw
# print raw data
pprint(location)