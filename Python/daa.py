# ============ DESIGN & ANALYSIS OF ALGORITHMS (DAA) - COMPLETE PYTHON ============
# All major algorithmic approaches with explanations and implementations

# ============ 1. TWO POINTER APPROACH ============
"""
CONCEPT: Use two pointers (left and right) to traverse from opposite ends or same end
WHEN: Sorted arrays, palindromes, target pairs, container with most water
TIME: Usually O(n), much faster than nested loops O(n²)
IDEA: Move pointers based on condition - if sum too small move left ptr, if too big move right ptr
"""

def two_pointer_sum_pair(arr, target):
    """Find pair of numbers that sum to target in sorted array"""
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [arr[left], arr[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None


def two_pointer_reverse_array(arr):
    """Reverse array using two pointers"""
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def two_pointer_partition(arr):
    """Partition array into even and odd numbers"""
    left, right = 0, len(arr) - 1
    while left < right:
        while left < right and arr[left] % 2 == 0:
            left += 1
        while left < right and arr[right] % 2 == 1:
            right -= 1
        arr[left], arr[right] = arr[right], arr[left]
    return arr


def container_with_most_water(height):
    """Maximum area between two vertical lines using two pointers"""
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_area = max(max_area, area)

        # Move pointer pointing to shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# ============ 2. SLIDING WINDOW APPROACH ============
"""
CONCEPT: Maintain a window of fixed or variable size, slide it across array
WHEN: Subarray problems, longest substring, max sum subarray
TIME: O(n) instead of O(n²) for nested loops
IDEA: Expand window by adding right element, shrink by removing left element when needed
"""

def sliding_window_max_sum(arr, k):
    """Maximum sum of subarray of size k"""
    if k > len(arr):
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_substring_without_repeating(s):
    """Longest substring without repeating characters"""
    char_index = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        if s[end] in char_index:
            start = max(start, char_index[s[end]] + 1)

        char_index[s[end]] = end
        max_length = max(max_length, end - start + 1)

    return max_length


def min_window_substring(s, t):
    """Minimum window substring that contains all chars of t"""
    if not s or not t:
        return ""

    required = {c: t.count(c) for c in t}
    left, right = 0, 0
    formed = 0
    window_counts = {}
    result = float('inf'), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in required and window_counts[char] == required[char]:
            formed += 1

        while left <= right and formed == len(required):
            char = s[left]
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)

            window_counts[char] -= 1
            if char in required and window_counts[char] < required[char]:
                formed -= 1

            left += 1

        right += 1

    return s[result[1]:result[2]+1] if result[0] != float('inf') else ""


# ============ 3. DYNAMIC PROGRAMMING ============

# 0/1 Knapsack
def knapsack_01(weights, values, capacity):
    """0/1 Knapsack: each item taken 0 or 1 time"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                             dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]


# Unbounded Knapsack
def knapsack_unbounded(weights, values, capacity):
    """Unbounded Knapsack: items can be used multiple times"""
    dp = [0] * (capacity + 1)

    for i in range(1, capacity + 1):
        for j in range(len(weights)):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])

    return dp[capacity]


# ============ 4. LONGEST COMMON SUBSEQUENCE (LCS) ============

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


def lcs_string(text1, text2):
    """Return the actual LCS string"""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Reconstruct string
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            result.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(result))


# ============ 5. LONGEST INCREASING SUBSEQUENCE (LIS) ============

def lis_length(arr):
    """Length of longest increasing subsequence"""
    n = len(arr)
    if n == 0:
        return 0

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_elements(arr):
    """Return actual elements of LIS"""
    n = len(arr)
    if n == 0:
        return []

    dp = [1] * n
    parent = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j

    max_idx = dp.index(max(dp))
    result = []
    while max_idx != -1:
        result.append(arr[max_idx])
        max_idx = parent[max_idx]

    return list(reversed(result))


# ============ 6. EDIT DISTANCE (Levenshtein Distance) ============

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
                dp[i][j] = 1 + min(dp[i-1][j],      # delete
                                   dp[i][j-1],      # insert
                                   dp[i-1][j-1])    # replace

    return dp[m][n]


# ============ 7. COIN CHANGE ============

def coin_change(coins, amount):
    """Minimum coins needed to make amount"""
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


# ============ 8. MATRIX CHAIN MULTIPLICATION ============

def matrix_chain_order(dimensions):
    """Minimum multiplications needed"""
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


# ============ 9. BINARY SEARCH ============

def binary_search(arr, target):
    """Standard binary search"""
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
    """First occurrence of target"""
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


# ============ 10. GREEDY ALGORITHMS ============

def activity_selection(activities):
    """Select max non-overlapping activities"""
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]

    for i in range(1, len(activities)):
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])

    return selected


def fractional_knapsack(items, capacity):
    """Fractional knapsack - can take fraction of items"""
    items_with_ratio = [(v/w, w, v) for w, v in items]
    items_with_ratio.sort(reverse=True)

    total_value = 0
    for ratio, weight, value in items_with_ratio:
        if capacity <= 0:
            break
        take = min(capacity, weight)
        total_value += take * ratio
        capacity -= take

    return total_value


# ============ 11. RECURSION WITH MEMOIZATION ============

def fib_memo(n, memo=None):
    """Fibonacci with memoization"""
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# ============ 12. GRAPH ALGORITHMS ============

def is_bipartite(graph, n):
    """Check if graph is bipartite using BFS"""
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        queue = [start]
        color[start] = 0

        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False

    return True


# ============ 13. DIVIDE AND CONQUER ============

def merge_sort(arr):
    """Merge sort - divide and conquer"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ============ 14. BACKTRACKING ============

def permutations(nums):
    """Generate all permutations"""
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):
            backtrack(path + [remaining[i]],
                     remaining[:i] + remaining[i+1:])

    backtrack([], nums)
    return result


def combinations(nums, r):
    """Generate all combinations of size r"""
    result = []

    def backtrack(start, path):
        if len(path) == r:
            result.append(path)
            return

        for i in range(start, len(nums)):
            backtrack(i + 1, path + [nums[i]])

    backtrack(0, [])
    return result
