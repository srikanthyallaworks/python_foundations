import requests


def get_geolocation_uri():
    return 'http://www.geoplugin.net/json.gp'


def get_gridlocation_uri(latitude, longitude):
    return f'https://api.weather.gov/points/{latitude},{longitude}'


def get_forecast_uri(office, x, y):
    return f'https://api.weather.gov/gridpoints/{office}/{x},{y}/forecast'


class GeoLocation:
    """Simple type to hold lat/long coordinates
    """

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


class GridLocation:
    """Simple type to hold coordinates used by weather.gov
    """

    def __init__(self, office, x, y):
        self.office = office
        self.x = x
        self.y = y


def fetch_json(uri):
    """Invokes the uri via GET

    Args:
        uri (str): Json endpoint

    Raises:
        ConnectionError: If the endpoint refuses 

    Returns:
        [dict]: Response json as a dict
    """
    response = requests.get(uri)
    if response.status_code != 200:
        raise ConnectionError("Couldn't Connect")
    json = response.json()
    response.close()
    return json


def get_geo_location():
    """Invokes a free web service to get a guess of the current
       IP's location

    Returns:
        [GeoLocation]: Lat/Long guess of the current location
    """
    uri = get_geolocation_uri()
    json = fetch_json(uri)
    return GeoLocation(
        latitude=float(json["geoplugin_latitude"]),
        longitude=float(json["geoplugin_longitude"])
    )


def get_grid_location(geo):
    """Gets a weather.gov coordinates of the specified lat/long  coordinates

    Args:
        geo (GeoLocation): lat/long to translate

    Returns:
        GridLocation: Location used by weather.gov to get a forecast
    """
    url = get_gridlocation_uri(geo.latitude, geo.longitude)
    json = fetch_json(url)["properties"]
    return GridLocation(
        office=json["cwa"],
        x=int(json["gridX"]),
        y=int(json["gridY"])
    )


def get_forecast(grid_loc):
    """Hits up weather.gove to gets a short forcast for the specified grid location

    Args:
        loc (GridLocation): location to forecast

    Returns:
        str: Short forecast of the next couple hours
    """
    url = get_forecast_uri(grid_loc.office, grid_loc.x, grid_loc.y)
    json = fetch_json(url)
    return json["properties"]["periods"][0]["shortForecast"]


def main():
    """Hits public APIs to get a short forcast for the local weather.
    """
    geo_location = get_geo_location()
    grid_location = get_grid_location(geo_location)
    forecast = get_forecast(grid_location)

    print(f'\n\nForecast:\n     {forecast}\n\n')


if __name__ == "__main__":
    main()
