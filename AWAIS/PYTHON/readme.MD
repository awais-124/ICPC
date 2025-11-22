# Python Competition Utilities

Comprehensive utility library for programming competitions. All functions include descriptive comments.

## Files Included:

1. `io_utils.py` - Fast input/output operations

   - Fast reading of integers, floats, strings, arrays
   - Efficient output for arrays and matrices

2. `math_utils.py` - Basic mathematical functions

   - Prime checking, factorization, divisors
   - GCD, LCM, combinatorics

3. `advanced_math.py` - Advanced mathematical functions

   - Modular arithmetic, exponentiation
   - Chinese Remainder Theorem, Sieve of Eratosthenes
   - Factorial and nCr with modulo

4. `array_utils.py` - Array/list operations

   - Prefix/suffix sums, frequency counting
   - Matrix rotations and transformations

5. `string_utils.py` - String algorithms

   - Pattern matching (KMP, Z-algorithm)
   - Palindrome detection (Manacher's)
   - String transformations

6. `graph_utils.py` - Graph algorithms

   - BFS, DFS, Dijkstra, Topological sort
   - Common graph traversals

7. `geometry_utils.py` - Geometry utilities

   - Point operations, line intersections
   - Convex hull, distance calculations

8. `bit_manipulation.py` - Bit manipulation

   - Bit checking, setting, clearing
   - Subset generation, power of two checks

9. `data_structure_utils.py` - Data structure implementations

   - Stack, Queue, PriorityQueue classes
   - 2D list operations, frequency analysis

10. `python_basics.py` - Python built-in helpers

    - List, string, dictionary operations
    - Sorting, permutations, combinations
    - Type conversion utilities

11. `misc_utils.py` - Miscellaneous utilities

    - Timing decorator, binary search
    - Memoization, random array generation

12. `debug_utils.py` - Debugging and testing

    - Time measurement, test case generation
    - Assertion helpers, pretty printing

13. `constants.py` - Common constants

    - Mathematical constants, direction arrays
    - ASCII values, common mod values

14. `competition_template.py` - Solution template
    - Ready-to-use competition template
    - Pre-configured imports and structure

## Usage:

Since you submit single files, copy the needed functions directly into your solution.
Use the comments to understand what each function does.

Example for quick copying:

```python
# Copy these GCD/LCM functions when needed:
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0
```

Tips:

- Use io_utils for fast input/output in problems with large I/O
- Use advanced_math for number theory problems
- Use bit_manipulation for problems involving bits and subsets
- Use debug_utils during development and testing
- Start with competition_template.py for new problems

These files now include comprehensive comments and cover virtually all common competition scenarios. You can quickly copy the functions you need into your solution file!
