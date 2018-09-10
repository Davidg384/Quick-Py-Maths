import math


def f(x, y):
    return x + y


def euler_method(a, b, n, i):
    """
    Approximates a numerical solution to an ordinary differential equation.
    :param i: The initial value
    :param a: The left bound of integration
    :param b: The right bound of integration
    :return: The approximation
    """
    h = (b-a)/n
    for step in range(n):
        approximation = i + h*f(a, i)
        i = approximation
        a += h
    return approximation


print(euler_method(0, 2, 50, 1))
