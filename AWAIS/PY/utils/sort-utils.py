# ---------- MERGE SORT ----------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    return res + a[i:] + b[j:]

# ---------- QUICK SORT ----------
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# ---------- COUNTING SORT ----------
def counting_sort(arr, maxv=None):
    if maxv is None:
        maxv = max(arr)
    cnt = [0]*(maxv+1)
    for x in arr:
        cnt[x] += 1
    res = []
    for i in range(maxv+1):
        res.extend([i]*cnt[i])
    return res
