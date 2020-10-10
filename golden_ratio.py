from functions import f
from constants import tau


def golden_ratio(a, b, eps):
    x_1 = b - (b - a) / tau
    x_2 = a + (b - a) / tau
    fx1 = f(x_1)
    fx2 = f(x_2)
    iterations = 0
    while (b - a) / 2 > eps:
        iterations += 1
        if fx1 > fx2:
            a = x_1
            x_1 = x_2
            x_2 = b - (x_1 - a)
            fx1 = fx2
            fx2 = f(x_2)
        else:
            b = x_2
            x_2 = x_1
            x_1 = a + (b - x_2)
            fx2 = fx1
            fx1 = f(x_1)
    return (a + b) / 2, f((a + b) / 2), iterations
