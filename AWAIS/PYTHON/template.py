#!/usr/bin/env python3
"""
Competition Solution Template
Copy this template for each problem solution
"""

import sys
from math_utils import *
from io_utils import *

# Uncomment the imports you need for specific problems
# from array_utils import *
# from string_utils import *
# from graph_utils import *
# from geometry_utils import *
# from bit_manipulation import *

def solve():
    """
    Main solution function
    Modify this function for each problem
    """
    # Example: Read number of test cases
    t = get_int()

    for _ in range(t):
        # Read input for each test case
        n = get_int()
        arr = get_ints()

        # Your solution logic here
        result = sum(arr)  # Example operation

        # Output the result
        print(result)

if __name__ == "__main__":
    # Add timing for performance measurement
    # start_time = time.time()

    solve()

    # Uncomment to measure total execution time
    # end_time = time.time()
    # print(f"Total execution time: {end_time - start_time:.3f}s", file=sys.stderr)
