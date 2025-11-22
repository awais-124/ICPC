# MATHEMATICAL ALGORITHMS - Common patterns for ICPC

# ============ GCD & LCM ============

# Greatest Common Divisor using Euclidean algorithm
def gcd(a, b):
    """GCD using Euclidean algorithm - O(log min(a,b))"""
    while b:
        a, b = b, a % b
    return a


# Least Common Multiple
def lcm(a, b):
    """LCM using GCD - lcm(a,b) = (a*b) / gcd(a,b)"""
    return (a * b) // gcd(a, b)


# Python built-in
from math import gcd as math_gcd


# ============ PRIME NUMBERS ============

def is_prime(n):
    """Check if n is prime - O(sqrt(n))"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """Generate all primes up to n - O(n log log n)"""
    is_prime_arr = [True] * (n + 1)
    is_prime_arr[0] = is_prime_arr[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime_arr[i]:
            for j in range(i*i, n + 1, i):
                is_prime_arr[j] = False

    return [i for i in range(n + 1) if is_prime_arr[i]]


def prime_factorization(n):
    """Find prime factors - returns dict {prime: count}"""
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


# ============ MODULAR ARITHMETIC ============

def mod_add(a, b, mod):
    """(a + b) % mod"""
    return (a + b) % mod


def mod_subtract(a, b, mod):
    """(a - b) % mod"""
    return (a - b + mod) % mod


def mod_multiply(a, b, mod):
    """(a * b) % mod"""
    return (a * b) % mod


def mod_power(base, exp, mod):
    """(base^exp) % mod using fast exponentiation"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result


def mod_inverse(a, mod):
    """Find modular inverse (a^-1 mod p) using Fermat's Little Theorem"""
    # Works when mod is prime: a^-1 ≡ a^(p-2) mod p
    return mod_power(a, mod - 2, mod)


def extended_gcd(a, b):
    """Extended Euclidean algorithm - finds x, y such that ax + by = gcd(a,b)"""
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y


# ============ COMBINATORICS WITH MOD ============

MOD = 10**9 + 7

def factorial_mod(n, mod=MOD):
    """Calculate n! % mod"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result


def nCr_mod(n, r, mod=MOD):
    """Calculate C(n,r) % mod using factorials and modular inverse"""
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1

    num = factorial_mod(n, mod)
    den = (factorial_mod(r, mod) * factorial_mod(n - r, mod)) % mod
    return (num * mod_inverse(den, mod)) % mod


# ============ NUMBER THEORY ============

def euler_totient(n):
    """Count numbers <= n that are coprime with n"""
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


def digit_sum(n):
    """Sum of digits of n"""
    total = 0
    while n:
        total += n % 10
        n //= 10
    return total


def digit_root(n):
    """Digital root - keep summing digits until single digit"""
    while n >= 10:
        n = digit_sum(n)
    return n


def count_digits(n):
    """Count number of digits"""
    return len(str(abs(n)))


# ============ POWER & EXPONENTIAL ============

def fast_power(base, exp):
    """Calculate base^exp efficiently - O(log exp)"""
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result


def is_power_of_two(n):
    """Check if n is power of 2 - O(1)"""
    return n > 0 and (n & (n - 1)) == 0


def power_of_two_less_than(n):
    """Find largest power of 2 less than n"""
    power = 1
    while power * 2 < n:
        power *= 2
    return power


# ============ GEOMETRIC & ALGEBRA ============

def gcd_of_array(arr):
    """GCD of all elements in array"""
    from functools import reduce
    return reduce(gcd, arr)


def lcm_of_array(arr):
    """LCM of all elements in array"""
    from functools import reduce
    return reduce(lcm, arr)


def solve_linear_equation(a, b, c):
    """Solve ax + b = c. Returns x"""
    if a == 0:
        return None
    return (c - b) / a


def is_perfect_square(n):
    """Check if n is perfect square"""
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n


def fibonacci(n):
    """Generate nth Fibonacci number"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def catalan(n):
    """nth Catalan number = C(2n, n) / (n+1)"""
    from math import comb
    return comb(2*n, n) // (n + 1)


# ============ BIT MANIPULATION ============

def set_bit(num, pos):
    """Set bit at position pos"""
    return num | (1 << pos)


def clear_bit(num, pos):
    """Clear bit at position pos"""
    return num & ~(1 << pos)


def toggle_bit(num, pos):
    """Toggle bit at position pos"""
    return num ^ (1 << pos)


def check_bit(num, pos):
    """Check if bit at position pos is set"""
    return (num >> pos) & 1


def count_set_bits(n):
    """Count number of 1s in binary representation"""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def lowest_set_bit(n):
    """Get lowest set bit position"""
    return (n & -n).bit_length() - 1


# ============ BINARY SEARCH ============

def binary_search(arr, target):
    """Find target in sorted array - O(log n)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_first(arr, target):
    """Find first occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def binary_search_last(arr, target):
    """Find last occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
