# Next, import the library
import geoip2.webservice

# Set your user ID and license key
user_id = 810838
license_key = "IN21rmrxSV7w80kx" 

# Use the geoip2.webservice.Client class to create a client object
client = geoip2.webservice.Client(user_id, license_key)

# Use the client's city() method to get the user's location
response = client.city(ip_address='me')

# Print the location
print(response)
