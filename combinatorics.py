def factorial(n):
    """
    Caluculates n!
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def permutation(n, k):
    return factorial(n)//factorial(n-k)


def choose(n, k):
    return permutation(n, k)//factorial(k)


def rising_fac(n, k):
    return factorial(n+k-1)//factorial(n-1)


def multichoose(n, k):
    return choose(n+k-1, k)


def multichoose2(n, k):
    return rising_fac(n, k)//factorial(k)


print(factorial(5), permutation(5, 3), choose(5, 3), multichoose(5, 3), multichoose2(5, 3), permutation(5, 5))

