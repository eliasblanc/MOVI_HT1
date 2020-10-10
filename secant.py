from functions import f, df


def secant(x0, x1, eps):
    iterations = 0
    tmp = 0
    while abs(x1 - x0) > eps:
        iterations += 1
        tmp = x1
        x1 = x1 - (x1 - x0) * df(x1) / (df(x1) - df(x0))
        x0 = tmp
    return x1, f(x1), iterations
