def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def permutation(n, k):
    p = factorial(n)//factorial(n-k)
    return p


def choose(n, k):
    c = permutation(n, k)//factorial(k)
    return c


def rising_fac(n, k):
    r = factorial(n+k-1)//factorial(n-1)
    return r


def multichoose(n, k):
    m = choose(n+k-1, k)
    return m

def multichoose2(n, k):
    m = rising_fac(n, k)//factorial(k)
    return m


print(factorial(5), permutation(5, 3), choose(5, 3), multichoose(5, 3), multichoose2(5, 3))
