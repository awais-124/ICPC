# ============ PYTHON TEMPLATES FOR ICPC ============
# Use these as starting points for your solutions

# ============ TEMPLATE 1: SINGLE TEST CASE ============

def solve():
    """Solve single test case"""
    # Read input
    n = int(input())
    arr = list(map(int, input().split()))

    # Your solution here
    result = sum(arr)

    # Output
    print(result)


if __name__ == "__main__":
    solve()


# ============ TEMPLATE 2: MULTIPLE TEST CASES ============

def solve():
    """Solve single test case"""
    n = int(input())
    arr = list(map(int, input().split()))

    # Your solution
    result = sum(arr)
    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 3: MULTIPLE TEST CASES (Variant) ============

def main():
    t = int(input())
    while t:
        t -= 1

        # Read input
        n = int(input())
        arr = list(map(int, input().split()))

        # Solve
        result = sum(arr)

        # Output
        print(result)


if __name__ == "__main__":
    main()


# ============ TEMPLATE 4: WITH HELPER FUNCTIONS ============

def read_input():
    """Read and parse input"""
    n = int(input())
    arr = list(map(int, input().split()))
    return n, arr


def solve(n, arr):
    """Main solution logic"""
    result = sum(arr)
    return result


def main():
    t = int(input())
    for _ in range(t):
        n, arr = read_input()
        result = solve(n, arr)
        print(result)


if __name__ == "__main__":
    main()


# ============ TEMPLATE 5: GRAPH PROBLEM ============

from collections import defaultdict, deque

def solve():
    n, m = map(int, input().split())

    # Build graph
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # BFS
    visited = set()
    queue = deque([1])
    visited.add(1)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print(len(visited))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()


# ============ TEMPLATE 6: DP PROBLEM ============

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # DP table
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], arr[i-1] + dp[max(0, i-2)])

    return dp[n]


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 7: MATH/NUMBER PROBLEM ============

MOD = 10**9 + 7

def power_mod(base, exp, mod=MOD):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result


def solve():
    n = int(input())
    a, b = map(int, input().split())

    # Your calculation
    result = power_mod(a, b)

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 8: SORTING/ARRAY PROBLEM ============

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Sort by custom criteria
    arr.sort(key=lambda x: (x % 2, x))  # Even first, then odd

    # Two pointers
    left, right = 0, n - 1
    result = 0

    while left < right:
        result += arr[left] + arr[right]
        left += 1
        right -= 1

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 9: STRING PROBLEM ============

def solve():
    s = input().strip()
    n = len(s)

    # Process string
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1

    # Find answer
    result = len(char_count)

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 10: COMPLEX I/O ============

def solve():
    # Multiple input lines
    line1 = list(map(int, input().split()))
    n, m = line1[0], line1[1]

    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    # Process
    result = 0
    for row in grid:
        result += sum(row)

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 11: QUICK DEBUG TEMPLATE ============

import sys
from collections import defaultdict, deque, Counter
from math import gcd, lcm, sqrt, ceil, floor

def solve():
    n = int(input())
    arr = list(map(int, input().split()))

    # Debug: print to stderr
    # print(f"Debug: n={n}, arr={arr}", file=sys.stderr)

    result = sum(arr)
    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())


# ============ TEMPLATE 12: WITH CLASS STRUCTURE ============

class Solution:
    def __init__(self):
        self.n = 0
        self.arr = []

    def read_input(self):
        self.n = int(input())
        self.arr = list(map(int, input().split()))

    def solve(self):
        # Your solution
        return sum(self.arr)

    def main(self):
        t = int(input())
        for _ in range(t):
            self.read_input()
            result = self.solve()
            print(result)


if __name__ == "__main__":
    solution = Solution()
    solution.main()


# ============ QUICK COPY-PASTE TEMPLATE (RECOMMENDED) ============

"""
Use this for most problems:
"""

def solve():
    n = int(input())
    # Add more reads here

    # Your solution

    return result


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        print(solve())
