import json
import requests
#f6f227bea0c24040978115410242407
def get_weather(city):
    '''
    Fetch city info from API
    '''
    # Define url and API 
    key = 'f6f227bea0c24040978115410242407'
    url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={city}"
    
    # Define get function
    response = requests.get(url)
    data = response.json()

    return data
for i in get_weather('Zugdidi'):
  print(i)
