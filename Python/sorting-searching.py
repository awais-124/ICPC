# SORTING & SEARCHING ALGORITHMS - All major techniques

# ============ PYTHON'S BUILT-IN SORTING ============

arr = [3, 1, 4, 1, 5, 9, 2, 6]

# In-place sort
arr.sort()                                     # [1, 1, 2, 3, 4, 5, 6, 9]
arr.sort(reverse=True)                         # [9, 6, 5, 4, 3, 2, 1, 1]

# Returns new sorted list
sorted(arr)                                    # [1, 1, 2, 3, 4, 5, 6, 9]
sorted(arr, reverse=True)

# Sort by custom key
words = ['apple', 'pie', 'a']
sorted(words, key=len)                         # ['a', 'pie', 'apple']

pairs = [(2, 'b'), (1, 'a'), (1, 'c')]
sorted(pairs, key=lambda x: (x[0], x[1]))    # [(1,'a'), (1,'c'), (2,'b')]

# Python uses Timsort: O(n log n) average and worst case


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


def binary_search_leftmost(arr, target):
    """Find leftmost (first) occurrence - O(log n)"""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1              # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def binary_search_rightmost(arr, target):
    """Find rightmost (last) occurrence - O(log n)"""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1               # Keep searching right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# Python's bisect module
import bisect

arr = [1, 3, 3, 3, 5, 7]
bisect.bisect_left(arr, 3)                     # 1 (leftmost insertion point)
bisect.bisect_right(arr, 3)                    # 4 (rightmost insertion point)
bisect.bisect(arr, 3)                          # 4 (same as bisect_right)

bisect.insort(arr, 4)                          # Insert maintaining sorted order


# ============ MERGE SORT ============
# O(n log n) - Stable, divide and conquer

def merge_sort(arr):
    """Divide array and merge sorted subarrays"""
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


# ============ QUICK SORT ============
# O(n log n) average, O(n²) worst - In-place, not stable

def quick_sort(arr):
    """Partition and recursively sort"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """In-place quick sort"""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)

    return arr


def partition(arr, low, high):
    """Partition around pivot"""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ============ SELECTION ALGORITHMS ============

# Find kth smallest element
def find_kth_smallest(arr, k):
    """Find kth smallest (1-indexed)"""
    sorted_arr = sorted(arr)
    return sorted_arr[k - 1]


def find_kth_smallest_quickselect(arr, k):
    """O(n) average using quickselect"""
    def quickselect(low, high, k_idx):
        if low == high:
            return arr[low]

        pivot_idx = partition(arr, low, high)

        if k_idx == pivot_idx:
            return arr[k_idx]
        elif k_idx < pivot_idx:
            return quickselect(low, pivot_idx - 1, k_idx)
        else:
            return quickselect(pivot_idx + 1, high, k_idx)

    return quickselect(0, len(arr) - 1, k - 1)


# ============ COUNTING SORT ============
# O(n + k) where k is range of input - Limited to small ranges

def counting_sort(arr, max_val):
    """Sort array of non-negative integers"""
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    idx = 0
    for i in range(max_val + 1):
        for _ in range(count[i]):
            arr[idx] = i
            idx += 1

    return arr


# ============ RADIX SORT ============
# O(d * n) where d is number of digits

def radix_sort(arr):
    """Sort by each digit position"""
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10

    return arr


def counting_sort_by_digit(arr, exp):
    """Counting sort by digit at position exp"""
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        count[(num // exp) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]


# ============ SEARCHING TECHNIQUES ============

# Linear Search
def linear_search(arr, target):
    """Search in unsorted array - O(n)"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Exponential Search (for sorted arrays)
def exponential_search(arr, target):
    """Find range where element may exist, then binary search"""
    if arr[0] == target:
        return 0

    i = 1
    while i < len(arr) and arr[i] < target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, len(arr)))


def binary_search(arr, target, left, right):
    """Helper for exponential search"""
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ============ SORTING STABILITY TEST ============

# Stable: maintains relative order of equal elements
# Merge sort: Stable, Quick sort: Not stable, Python's sort: Stable

pairs = [(1, 'a'), (2, 'b'), (1, 'c')]
sorted(pairs, key=lambda x: x[0])
# Result: [(1, 'a'), (1, 'c'), (2, 'b')] - order of (1,'a') and (1,'c') preserved


# ============ TWO POINTERS FOR SORTED ARRAYS ============

def two_sum_sorted(arr, target):
    """Find two numbers that sum to target - O(n)"""
    left, right = 0, len(arr) - 1

    while left < right:
        total = arr[left] + arr[right]
        if total == target:
            return [arr[left], arr[right]]
        elif total < target:
            left += 1
        else:
            right -= 1

    return None
