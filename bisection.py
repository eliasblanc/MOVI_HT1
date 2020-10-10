from functions import f, df


def bisection(a, b, eps):
	x = (a + b) / 2
	iterations = 0
	if df(a) * df(b) < 0:
		while (b - a) / 2 > eps:
			iterations += 1
			dfa0 = df(x)
			if dfa0 * df(b) < 0:
				a = x
				x = (a + b) / 2
			elif df(a) * dfa0 < 0:
				b = x
				x = (a + b) / 2
			else:
				return x, f(x), iterations
		return x, f(x), iterations
	elif df(a) * df(b) > 0:
		print(f"There are no roots on the [{a}, {b}]")
		return
	else:
		return x, f(x), iterations
