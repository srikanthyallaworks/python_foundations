import requests


def get_geolocation_uri():
  return 'http://www.geoplugin.net/json.gp'

def get_gridlocation_uri(latitude,longitude):
  return f'https://api.weather.gov/points/{latitude},{longitude}'

def get_forecast_uri(office,x,y):
  return f'https://api.weather.gov/gridpoints/{office}/{x},{y}/forecast'




def get_geo_location():
  """Invokes a free web service to get a guess of the current
     IP's location

  Returns:
      [GeoLocation]: Lat/Long guess of the current location
  """
  uri = get_geolocation_uri()
  response = requests.get(uri)
  if response.status_code != 200:
    raise ConnectionError("Couldn't Connect")
  response.close()
  return response.json()




def main():
  """Hits public APIs to get a short forcast for the local weather.
  """
  geo_location = get_geo_location()
  print(f'Here is your geo location: {geo_location}')
  # TODO: Figure out the forecast too



if __name__ == "__main__":
    main()

