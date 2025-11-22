import math

# ---------- BASIC ----------
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a // gcd(a, b) * b

# ---------- FAST POWER ----------
def modpow(a, b, mod):
    res = 1
    a %= mod
    while b:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res

# ---------- MODULAR INVERSE ----------
def modinv(a, mod):
    return modpow(a, mod - 2, mod)

# ---------- FACTORIALS + NCR ----------
def build_factorials(n, mod):
    fact = [1] * (n + 1)
    invfact = [1] * (n + 1)

    for i in range(1, n + 1):
        fact[i] = fact[i - 1] * i % mod

    invfact[n] = modinv(fact[n], mod)
    for i in reversed(range(n)):
        invfact[i] = invfact[i + 1] * (i + 1) % mod

    return fact, invfact

def nCr(n, r, fact, invfact, mod):
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % mod * invfact[n - r] % mod

# ---------- SIEVE ----------
def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    return prime

def prime_list(n):
    primes = []
    arr = sieve(n)
    for i in range(n + 1):
        if arr[i]:
            primes.append(i)
    return primes

# ---------- PRIME FACTORIZATION ----------
def prime_factors(n):
    res = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            res.append(d)
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res

# ---------- SEGMENTED SIEVE ----------
def segmented_sieve(l, r):
    import math
    limit = int(math.sqrt(r)) + 1
    primes = prime_list(limit)
    mark = [True] * (r - l + 1)

    for p in primes:
        start = max(p * p, (l + p - 1) // p * p)
        for j in range(start, r + 1, p):
            mark[j - l] = False

    if l == 1:
        mark[0] = False

    res = []
    for i in range(r - l + 1):
        if mark[i]:
            res.append(l + i)
    return res

# ---------- TOTIENT ----------
def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result
