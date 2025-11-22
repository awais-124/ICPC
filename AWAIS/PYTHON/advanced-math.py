import math

def gcd(a, b):
    """Compute Greatest Common Divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Compute Least Common Multiple of two numbers"""
    return abs(a * b) // gcd(a, b) if a and b else 0

def gcd_list(numbers):
    """Compute GCD of a list of numbers"""
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

def lcm_list(numbers):
    """Compute LCM of a list of numbers"""
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = lcm(result, numbers[i])
    return result

def modular_exponentiation(base, exponent, mod):
    """Compute (base^exponent) % mod efficiently using binary exponentiation"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result

def chinese_remainder_theorem(remainders, moduli):
    """Solve system of congruences: x ≡ remainders[i] (mod moduli[i])"""
    total = 0
    prod = math.prod(moduli)
    for r, m in zip(remainders, moduli):
        p = prod // m
        total += r * mod_inverse(p, m) * p
    return total % prod

def sieve_of_eratosthenes(n):
    """Generate all primes up to n using Sieve of Eratosthenes"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def factorial_mod(n, mod):
    """Compute n! % mod efficiently"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result

def nCr_mod(n, r, mod):
    """Compute nCr % mod using modular inverses"""
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1
    numerator = factorial_mod(n, mod)
    denominator = (factorial_mod(r, mod) * factorial_mod(n - r, mod)) % mod
    return (numerator * mod_inverse(denominator, mod)) % mod

def mod_inverse(a, m):
    """Compute modular inverse of a under modulo m using extended Euclidean algorithm"""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None  # modular inverse doesn't exist
    return (x % m + m) % m

def extended_gcd(a, b):
    """Extended Euclidean algorithm: returns (gcd, x, y) such that ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y
