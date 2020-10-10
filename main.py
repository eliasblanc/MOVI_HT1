from constants import *

from golden_ratio import golden_ratio
from bisection import bisection
from secant import secant


if __name__ == '__main__':

	print("\n GOLDEN RATIO")
	x, fx, it = golden_ratio(a, b, eps_1)
	print(f"\nfor eps = {eps_1}", "\nx* = ", x, "\nf(x*) = ", fx, "\niteration number = ", it)
	x, fx, it = golden_ratio(a, b, eps_2)
	print(f"\nfor eps = {eps_2}", "\nx* = ", x, "\nf(x*) = ", fx, "\niteration number = ", it)

	print("\n BISECTION")
	x, fx, it = bisection(a, b, eps_1)
	print(f"\nfor eps = {eps_1}", "\nx* = ", x, "\nf(x*) = ", fx, "\niteration number = ", it)
	x, fx, it = bisection(a, b, eps_2)
	print(f"\nfor eps = {eps_2}", "\nx* = ", x, "\nf(x*) = ", fx, "\niteration number = ", it)

	print("\n SECANT")
	x, fx, it = secant(a, b, eps_1)
	print(f"\nfor eps = {eps_1}", "\nx* = ", x, "\nf(x*) = ", fx, "\niteration number = ", it)
	x, fx, it = secant(1.7, 2, eps_2)
	print(f"\nfor eps = {eps_2}", "\nx* = ", x, "\nf(x*) = ", fx, "\niteration number = ", it)

	input("\n\nPRESS ANY KEY TO CLOSE")