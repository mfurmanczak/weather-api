import requests

# List of locations to retrieve weather updates for
def get_city():
    user_locations = ['San Francisco, CA', 'Lima, Chile', 'Bejing, China', 'Newcastle Upon Tyne, England','Warsaw, Poland',
                  'Berlin, Germany', 'Paris, France', 'Rome, Italy', 'Athens, Greece', 'Cairo, Egypt']
    for i in range(len(user_locations)):    
        print(i+1, user_locations[i])
    num_city = input()
    city = user_locations[int(num_city)-1]
    return city
    
def get_weather(city):
    url = 'https://wttr.in/{}'.format(city)
    res = requests.get(url)
    return res.text