def f(x):
    return 4**x + 5**x - 6**x


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
    print("Root for 4^x + 5^x - 6^x = 0")
    print("")
    print("x = " + str(bisection(2, 3, 0.000001)))
    print("")


main()
