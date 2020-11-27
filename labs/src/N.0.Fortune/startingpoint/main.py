"""

https://realpython.com/api-integration-in-python/


"""
import requests


def main():
    response = requests.get("http://api.kanye.rest/")
    print(response.json())


if __name__ == "__main__":
    main()

