"""
G19: Use Explanatory Variables (Testing)

One of the more powerful ways to make a program readable is to break the calculations up into intermediate
values that are held in variables with meaningful names. Consider the following example from FitNesse:

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/general/g19-use-explanatory-variables.html

"""
from unittest.mock import Mock


def _example_api_call(api_client):
    result = api_client.get(
        "https://spark-academy.com", 10, params={"testing": "is good", "counter": "1"}
    )
    # do something with result


def example2():
    # Given
    api_mock = Mock()

    # When
    _example_api_call(api_mock)

    # Then
    api_mock.get.assert_called_once()

    assert "https" in api_mock.get.call_args[0][0]
    assert 10 == api_mock.get.call_args[0][1]
    assert "params" in api_mock.get.call_args[1]
    print("====== TEST PASSED ======")


if __name__ == "__main__":
    example2()
