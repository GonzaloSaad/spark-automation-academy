"""
G20: Function Names Should Say What They Do

If you have to look at the implementation (or documentation) of the function to know
what it does, then you should work to ﬁnd a better name or rearrange the functionality so
that it can be placed in functions with better names.

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/general/g20-function-names-should-say-what-they-do.html
"""


import requests


def func(country):
    """
    Fetches a list of universities for a given country in UniversityAPI
    """
    params = {"country": country}
    result = requests.get("http://universities.hipolabs.com/search", params=params)
    universities = result.json()
    print(universities)


def example():
    country = "Argentina"
    func(country)


if __name__ == "__main__":
    example()
