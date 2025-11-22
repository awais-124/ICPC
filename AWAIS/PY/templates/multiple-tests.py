#!/usr/bin/env python3
# Template for multiple testcases (common in Codeforces/ICPC)

import sys
from utils.fast_io import input, read_int, read_ints, run_main

def solve_case():
    # handle a single test case; read input here
    n = read_int()
    arr = read_ints()
    # example output
    print(sum(arr))

def solve():
    t = read_int()
    for _ in range(t):
        solve_case()

if __name__ == "__main__":
    solve()
    # or use run_main(solve) if recursion/deep stack needed
