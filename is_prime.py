from random import randint

def small_is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if (n % i) == 0:
            return False
        return True


def is_prime(n, k=5):  # miller-rabin
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0: return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, int(d / 2)
    for i in range(k):
        x = pow(randint(2, n - 1), d, n)
        if x == 1 or x == n - 1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n - 1: break
        else:
            return False
    return True


def checkPrimes(numbers):
    for n in numbers:
        if is_prime(n):
            print('Prime')
        else:
            print('Not prime')


