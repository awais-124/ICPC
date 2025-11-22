# DYNAMIC PROGRAMMING & GREEDY - Common patterns and problems

# ============ DYNAMIC PROGRAMMING BASICS ============

# DP Strategy: Break problem into subproblems, store results to avoid recomputation
# Two approaches: Top-down (Memoization) & Bottom-up (Tabulation)

# 1. FIBONACCI
def fib_recursive(n):
    """Simple recursion - SLOW for large n"""
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_memo(n, memo=None):
    """Top-down: Memoization"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def fib_dp(n):
    """Bottom-up: Tabulation"""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# 2. 0/1 KNAPSACK PROBLEM
# Given items with weight and value, max capacity - find max value

def knapsack_01(weights, values, capacity):
    """Bottom-up DP"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item
            dp[i][w] = dp[i-1][w]

            # Take item if it fits
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])

    return dp[n][capacity]


# 3. LONGEST COMMON SUBSEQUENCE (LCS)
def lcs(text1, text2):
    """Find length of longest common subsequence"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]


# 4. COIN CHANGE - Minimum coins needed
def coin_change(coins, amount):
    """Find minimum number of coins to make amount"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_combinations(coins, amount):
    """Number of ways to make amount"""
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]


# 5. LONGEST INCREASING SUBSEQUENCE (LIS)
def lis_length(arr):
    """Find length of longest increasing subsequence"""
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# 6. EDIT DISTANCE (Levenshtein Distance)
def edit_distance(word1, word2):
    """Minimum operations to transform word1 to word2"""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[m][n]


# 7. MATRIX CHAIN MULTIPLICATION
def matrix_chain_order(dimensions):
    """Find minimum multiplications needed"""
    n = len(dimensions) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                ops = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                dp[i][j] = min(dp[i][j], ops)

    return dp[0][n-1]


# ============ GREEDY ALGORITHMS ============

# 1. ACTIVITY SELECTION - Select max non-overlapping activities
def activity_selection(activities):
    """activities: list of (start, end) tuples"""
    activities.sort(key=lambda x: x[1])  # Sort by end time
    selected = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])

    return selected


# 2. FRACTIONAL KNAPSACK
def fractional_knapsack(items, capacity):
    """items: (weight, value) tuples. Can take fraction of item"""
    items_with_ratio = [(v/w, w, v) for w, v in items]
    items_with_ratio.sort(reverse=True)  # Sort by value/weight ratio

    total_value = 0
    for ratio, weight, value in items_with_ratio:
        if capacity <= 0:
            break
        take = min(capacity, weight)
        total_value += take * ratio
        capacity -= take

    return total_value


# 3. HUFFMAN CODING (simplified structure)
import heapq

class HuffNode:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_tree(freq_dict):
    """Build Huffman tree from character frequencies"""
    heap = [HuffNode(freq, char) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffNode(left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    return heap[0]


# 4. INTERVAL SCHEDULING MAXIMIZATION
def interval_scheduling(intervals):
    """Greedy: sort by end time and pick non-overlapping"""
    intervals.sort(key=lambda x: x[1])
    selected = []
    last_end = 0

    for start, end in intervals:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


# ============ DP STATE COMPRESSION ============

# When DP table is 2D but one dimension is small, use only 2 rows

def fib_space_optimized(n):
    """Space-optimized Fibonacci - O(1) space instead of O(n)"""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1
