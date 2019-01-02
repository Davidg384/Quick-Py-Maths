#!/bin/python

def f(n):
    return 9**n + 10**n - 11**n


def bisection(a, b, tol):
    while(abs(f(a) - f(b) >= tol)):
        c = (b+a)/2
        if f(c) == 0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return c


def main():
    print("")
    print("n ~ " + str(bisection(4, 5, 0.000001)))
    print("")


main()
