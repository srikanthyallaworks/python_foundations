
import requests
from dataclasses import dataclass
from typing import Dict

@dataclass(frozen=True)
class GeoLocation:
  latitude:float
  longitude:float

@dataclass(frozen=True)
class GridLocation:
  office:str
  x:int
  y:int


def fetch(uri: str)->Dict:
  response = requests.get(uri)
  if response.status_code != 200:
    raise ConnectionError("Couldn't Connect")
  json = response.json()
  response.close()
  return json


def get_geo_location()->GeoLocation:
  json = fetch('http://www.geoplugin.net/json.gp')
  return GeoLocation(
    latitude= float(json["geoplugin_latitude"]),
    longitude=float(json["geoplugin_longitude"])
  )
  


def get_grid_location(geo:GeoLocation)->GridLocation:
  url = f'https://api.weather.gov/points/{geo.latitude},{geo.longitude}'
  json = fetch(url)["properties"]
  return GridLocation(
    office=json["cwa"],
    x=int(json["gridX"]),
    y=int(json["gridY"])
  )


def get_forecast(loc:GridLocation)->str:
  url = f'https://api.weather.gov/gridpoints/{loc.office}/{loc.x},{loc.y}/forecast'
  return fetch(url)["properties"]["periods"][0]["shortForecast"]



def get_local_forecast():
  geo_location = get_geo_location()
  grid_location = get_grid_location(geo_location)
  return get_forecast(grid_location)
