"""
G19: Use Explanatory Variables

One of the more powerful ways to make a program readable is to break the calculations up into intermediate
values that are held in variables with meaningful names. Consider the following example from FitNesse:

Docs:
    https://moderatemisbehaviour.github.io/clean-code-smells-and-heuristics/general/g19-use-explanatory-variables.html

"""


def example1():
    i = [4, 5, 6, 7]
    rslt = []
    for n in i:
        if n % 2 == 0:
            rslt.append(n)
    print(rslt)


if __name__ == "__main__":
    example1()
