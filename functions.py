import math


def f(x): return math.cosh(x ** 3 - 4 * x + 1)


def df(x): return (3 * x ** 2 - 4) * math.sinh(x ** 3 - 4 * x + 1)
