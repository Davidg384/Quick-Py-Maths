def factorial(n):
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


<<<<<<< HEAD
def multichoose2(n, k):
    return rising_fac(n, k)//factorial(k)
=======
print(factorial(5), permutation(5, 3), choose(5, 3), multichoose(5, 3), multichoose2(5, 3), permutaion(5,5))
>>>>>>> 21732ea6f814189f42b457790780c08d535550bd
