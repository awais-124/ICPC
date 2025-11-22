#!/usr/bin/env python3
# DP problem template: memoization + iterative patterns

import sys
from functools import lru_cache
from utils.fast_io import input, read_int, read_ints

# Example: Fibonacci with memo
@lru_cache(None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def solve():
    n = read_int()
    print(fib(n))

if __name__ == "__main__":
    solve()
