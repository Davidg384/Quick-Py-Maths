import math


def f(x):
    return 1-x**2


def left_reimann(a, b, n):
    dx = (b-a)/n
    l = a
    summation = 0
    for rectangles in range(n):
        summation += f(l)*dx
        l += dx
    return summation


def right_reimann(a, b, n):
    dx = (b-a)/n
    l = a+dx
    summation = 0
    for i in range(n):
        summation += f(l)*dx
        l += dx
    return summation


def trapezoidal_reimann(a, b, n):
    dx = (b-a)/n
    summation = 0
    l = a
    r = a+dx
    for trapezoid in range(n):
        summation += (f(l)+f(r))*dx/2
        l = r
        r += dx
    return summation


def simpson(a, b, n):
    dx = (b-a)/n
    l = a
    r = a+dx
    summation = 0
    for i in range(n):
        summation += (r-l)/6*(f(l)+4*f((l+r)/2)+f(r))
        l = r
        r += dx
    return summation

def trapazoid_richard_extrapolation(a, b, n1, n2):
    """
    Richardsons extrapolation is doing 2 trapazoidal rules with different n values
    then approximating the error that occurs between them.

    hj is the step-size of the first trapazodal rule
    hi is the step-size of the second one

    if hj = 2*(hi) then you can simplify into a nice formula.
    This is the case in the problem so we'll go with that...
    """
    hj = (b-a)/n1
    hi = (b-a)/n2
    first = trapezoidal_reimann(a, b, n1)
    second = trapezoidal_reimann(a, b, n2)
    print(first)
    print(second)
    integral = (4/3)*first - (1/3)*second
    return integral

def simpsons_richard_extrapolation(a, b, n1, n2):
    """
    Richardsons extrapolation is doing 2 trapazoidal rules with different n values
    then approximating the error that occurs between them.

    hj is the step-size of the first trapazodal rule
    hi is the step-size of the second one

    if hj = 2*(hi) then you can simplify into a nice formula.
    This is the case in the problem so we'll go with that...
    """
    hj = (b-a)/n1
    hi = (b-a)/n2
    first = simpson(a, b, n1)
    second = simpson(a, b, n2)
    print(first)
    print(second)
    integral = (4/3)*first - (1/3)*second
    return integral



def err_calc(actual, a, b, nlist):
    """
    Calculates error given actual answer and approximations
    :param actual: L
    :param a: a
    :param b: b
    :param nlist: list of n values to approximate reimann
    :return:
    """
    err_list = []
    app_list = []
    for n in nlist:
        err = abs(actual - simpson(a, b, n))
        err_list.append(err)
        app_list.append(simpson(a, b, n))
    return (app_list, err_list)


print(simpsons_richard_extrapolation(-1, 1, 128, 256))
