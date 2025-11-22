#!/usr/bin/env python3
# Basic contest template: fast IO + main wrapper.
# Usage: put solution logic in solve().

import sys
from utils.fast_io import input, read_ints, read_int, run_main, fast_output

def solve():
    # Example: read one int and print it doubled
    n = read_int()
    print(n * 2)

if __name__ == "__main__":
    # For recursion-heavy problems, uncomment run_main
    # run_main(solve)
    solve()
