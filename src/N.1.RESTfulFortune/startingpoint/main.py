import requests

cat_uri = "https://cat-fact.herokuapp.com/facts/random"
kanye_uri = "http://api.kanye.rest"


def get_fortune() -> str:
    """Gets a random quotation (or cat fact) from a public RESTful web service."""
    return "You will meet a mysterious stranger."


def main():
    message = get_fortune()
    print("\nYour fortune is:")
    print(f"   {message}\n\n")


if __name__ == "__main__":
    main()
