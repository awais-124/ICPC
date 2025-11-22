# ---------- BINARY SEARCH ----------
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l

def upper_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= x:
            l = mid + 1
        else:
            r = mid
    return l

# ---------- TERNARY SEARCH ----------
def ternary_search(f, left, right, eps=1e-9):
    while right - left > eps:
        m1 = left + (right - left)/3
        m2 = right - (right - left)/3
        if f(m1) < f(m2):
            left = m1
        else:
            right = m2
    return left

# ---------- TWO POINTERS ----------
def two_pointer_sum(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i] + arr[j]
        if s == target:
            return (i, j)
        if s < target:
            i += 1
        else:
            j -= 1
    return None
