from numpy.polynomial import Polynomial
from math import fabs


def find_roots(coefficients):
    p = Polynomial(coefficients)
    print "\nRoots of U(x) with E = %d are:" % fabs(coefficients[0])
    for i, r in enumerate(p.roots()):
        if r.imag != 0.0:
            sign = "-" if r.imag < 0 else "+"
            print "x%d: %.1f %s %.1fi" % (i+1, r.real, sign, fabs(r.imag))
        else:
            print "x%d: %.1f" % (i + 1, r.real)


if __name__ == '__main__':
    # Passing the coefficients of U(x) for E = 5
    find_roots([-5, 0, 6, -1/2., -1])

    # Passing the coefficients of U(x) for E = 15
    find_roots([-15, 0, 6, -1/2., -1])
