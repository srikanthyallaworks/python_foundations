import requests
from dataclasses import dataclass


@dataclass(frozen=True)
class GeoLocation:
    """Simple type to hold lat/long coordinates"""

    latitude: float
    longitude: float


@dataclass(frozen=True)
class GridLocation:
    """Simple type to hold coordinates used by weather.gov"""

    office: str
    x: int
    y: int


class Uris:
    def for_geolocation():
        return "http://www.geoplugin.net/json.gp"

    def for_gridlocation(loc: GeoLocation):
        return f"https://api.weather.gov/points/{loc.latitude},{loc.longitude}"

    def for_forecast(loc: GridLocation):
        return (
            f"https://api.weather.gov/gridpoints/{loc.office}/{loc.x},{loc.y}/forecast"
        )


def fetch_json(uri: str) -> dict:
    """Invokes the uri via GET

    Args:
        uri (str): Json endpoint

    Raises:
        ConnectionError: If the endpoint refuse

    Returns:
        [dict]: Response json as a dict
    """
    with requests.get(uri) as response:
        if response.status_code != 200:
            raise ConnectionError("Couldn't Connect")
        return response.json()


def get_geo_location() -> GeoLocation:
    """Invokes a free web service to get a guess of the current
       IP's location

    Returns:
        [GeoLocation]: Lat/Long guess of the current location
    """
    uri = Uris.for_geolocation()
    json = fetch_json(uri)
    return GeoLocation(
        latitude=float(json["geoplugin_latitude"]),
        longitude=float(json["geoplugin_longitude"]),
    )


def get_grid_location(geo: GeoLocation) -> GridLocation:
    """Gets a weather.gov coordinates of the specified lat/long  coordinates

    Args:
        geo (GeoLocation): lat/long to translate

    Returns:
        GridLocation: Location used by weather.gov to get a forecast
    """
    uri = Uris.for_gridlocation(geo)
    json = fetch_json(uri)["properties"]
    return GridLocation(office=json["cwa"], x=int(json["gridX"]), y=int(json["gridY"]))


def get_forecast(loc: GridLocation) -> str:
    """Hits up weather.gove to gets a short forcast for the specified grid location

    Args:
        loc (GridLocation): location to forecast

    Returns:
        str: Short forecast of the next couple hours
    """
    url = Uris.for_forecast(loc)
    return fetch_json(url)["properties"]["periods"][0]["shortForecast"]


def main():
    """Hits public APIs to get a short forcast for the local weather."""
    geo_location = get_geo_location()
    grid_location = get_grid_location(geo_location)
    forecast = get_forecast(grid_location)
    print(f"\n\nForecast:\n     {forecast}\n\n")


if __name__ == "__main__":
    main()
