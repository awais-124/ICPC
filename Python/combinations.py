# COMBINATORICS - Combinations, Permutations & Counting
# With and without repetitions

from math import factorial
from itertools import combinations, permutations, combinations_with_replacement, permutations
import itertools

# ============ FACTORIAL & BASIC COUNTING ============

def factorial_iterative(n):
    """Calculate n!"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ============ COMBINATIONS (ORDER DOESN'T MATTER) ============

# C(n, r) = n! / (r! * (n-r)!)

def combinations_formula(n, r):
    """Combinations without repetition using formula"""
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


def combinations_iterative(n, r):
    """Generate all combinations of size r from n items"""
    result = []
    indices = list(range(r))
    result.append(tuple(range(r)))

    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return result

        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1

        result.append(tuple(indices))


# Using Python's built-in
def get_combinations(items, r):
    """Get all combinations of size r from items"""
    return list(combinations(items, r))
    # Example: list(combinations([1,2,3], 2)) = [(1,2), (1,3), (2,3)]


# ============ COMBINATIONS WITH REPETITION ============

# Choose r items from n types, items can repeat
# Formula: C(n+r-1, r)

def combinations_with_rep(items, r):
    """Get all combinations with repetition allowed"""
    return list(combinations_with_replacement(items, r))
    # Example: list(combinations_with_replacement([1,2,3], 2))
    # = [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]


def count_combinations_with_rep(n, r):
    """Count combinations with repetition"""
    return combinations_formula(n + r - 1, r)


# ============ PERMUTATIONS (ORDER MATTERS) ============

# P(n, r) = n! / (n-r)!

def permutations_formula(n, r=None):
    """Permutations using formula"""
    if r is None:
        r = n
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)


def get_permutations(items, r=None):
    """Get all permutations of size r from items"""
    if r is None:
        r = len(items)
    return list(permutations(items, r))
    # Example: list(permutations([1,2,3], 2)) = [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]


def permutations_all(items):
    """Get all permutations (full length)"""
    return list(itertools.permutations(items))


# ============ PERMUTATIONS WITH REPETITION ============

# n^r (n items, r positions, each position can be any of n items)

def permutations_with_rep(items, r):
    """All permutations with repetition allowed"""
    return list(itertools.product(items, repeat=r))
    # Example: list(itertools.product([1,2], repeat=2)) = [(1,1), (1,2), (2,1), (2,2)]


def count_permutations_with_rep(n, r):
    """Count permutations with repetition"""
    return n ** r


# ============ MULTISET PERMUTATIONS ============

# When you have duplicates (like arranging letters in "AAB")
# Formula: n! / (n1! * n2! * ... * nk!)

def permutations_multiset(items):
    """Generate unique permutations for multiset"""
    # Using sorted() to handle duplicates
    return list(set(itertools.permutations(sorted(items))))


def count_multiset_permutations(freq_dict):
    """
    Count permutations when items have frequencies
    freq_dict: {item: frequency}
    Example: {'A': 2, 'B': 1} has 3!/(2!*1!) = 3 permutations
    """
    n = sum(freq_dict.values())
    result = factorial(n)
    for count in freq_dict.values():
        result //= factorial(count)
    return result


# ============ COMMON PATTERNS ============

# Pascal's Triangle (for computing binomial coefficients)
def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows"""
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)
    return triangle


# ============ MODULAR ARITHMETIC (For large factorials) ============

MOD = 10**9 + 7

def factorial_mod(n, mod=MOD):
    """Calculate n! % mod"""
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % mod
    return result


def mod_inverse(a, mod=MOD):
    """Calculate modular inverse using Fermat's little theorem (a^-1 ≡ a^(p-2) mod p)"""
    return pow(a, mod - 2, mod)


def combinations_mod(n, r, mod=MOD):
    """Calculate C(n,r) % mod"""
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1

    numerator = factorial_mod(n, mod)
    denominator = (factorial_mod(r, mod) * factorial_mod(n - r, mod)) % mod

    return (numerator * mod_inverse(denominator, mod)) % mod
