# ---------- MILLER-RABIN ----------
def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17]:
        if n == p:
            return True
        if n % p == 0:
            return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                return True
        return False

    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        if not check(a):
            return False
    return True

# ---------- POLLARD RHO ----------
import random
def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if is_prime(n):
        return n

    while True:
        x = random.randrange(2, n)
        y = x
        c = random.randrange(1, n)
        d = 1
        while d == 1:
            x = (x*x + c) % n
            y = (y*y + c) % n
            y = (y*y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d

# ---------- FACTORIZATION USING POLLARD ----------
def factorize(n):
    if n == 1:
        return []
    if is_prime(n):
        return [n]
    d = pollard_rho(n)
    return factorize(d) + factorize(n // d)

# ---------- DISCRETE LOG ----------
def discrete_log(a, b, mod):
    import math
    a %= mod; b %= mod
    if b == 1:
        return 0
    m = int(math.sqrt(mod) + 1)

    table = {}
    e = 1
    for j in range(m):
        table[e] = j
        e = e * a % mod

    factor = pow(a, mod - m - 1, mod)
    gamma = b
    for i in range(m):
        if gamma in table:
            return i * m + table[gamma]
        gamma = gamma * factor % mod
    return None
