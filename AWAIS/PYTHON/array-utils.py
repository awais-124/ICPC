def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]
    return prefix

def suffix_sum(arr):
    suffix = [0] * (len(arr) + 1)
    for i in range(len(arr) - 1, -1, -1):
        suffix[i] = suffix[i + 1] + arr[i]
    return suffix

def frequency_count(arr):
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

def rotate_matrix_90_clockwise(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def rotate_matrix_90_counterclockwise(matrix):
    return [list(row) for row in zip(*matrix)][::-1]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for x in arr:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return list(duplicates)
