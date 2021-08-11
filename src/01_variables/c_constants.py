"""
G25: Replace Magic Numbers with Named Constants

In general it is a bad idea to have raw numbers in your code.
You should hide them behind well-named constants.

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/general/g25-replace-magic-numbers-with-named-constants.html

"""
from datetime import datetime, timedelta


def example():
    # Let's convert to UTC-3 (Arg Time) like this was never written before
    now_utc = datetime.utcnow()
    arg_time = now_utc - timedelta(seconds=10800)
    print(arg_time)


if __name__ == "__main__":
    example()
