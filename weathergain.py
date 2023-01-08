import requests

# List of locations to retrieve weather updates for
locations = ['San Francisco, CA', 'New York, NY', 'Seattle, WA']

# API endpoint for getting weather updates
endpoint = 'https://wttr.in/'

# Retrieve weather updates for each location
for location in locations:
    response = requests.get(endpoint + location + '?format=%C%t%w')
    print(location + ': ' + response.text)
