"""
Chapter 3 - Small!

The first rule of functions is that they should be small.
The second rule of functions is that they should be smaller than that.

- FUNCTIONS SHOULD DO ONE THING.
- THEY SHOULD DO IT WELL.
- THEY SHOULD DO IT ONLY.

Still, everything comes in balance.
"""
import requests


def fetch_universities_by_country(country):
    """
    Fetches a list of universities for a given country in UniversityAPI
    """
    params = {"country": country}
    result = requests.get("http://universities.hipolabs.com/search", params=params)
    universities = result.json()
    print(universities)


def example():
    country = "Argentina              "
    fetch_universities_by_country(country)


if __name__ == "__main__":
    example()
