# ---------- KNAPSACK ----------
def knapsack(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w-weights[i]] + values[i])
    return dp[W]

# ---------- UNBOUNDED KNAPSACK ----------
def unbounded_knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        for w in range(weights[i], W + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[W]

# ---------- LIS ----------
def lis(arr):
    import bisect
    d = []
    for x in arr:
        i = bisect.bisect_left(d, x)
        if i == len(d):
            d.append(x)
        else:
            d[i] = x
    return len(d)

# ---------- MATRIX EXP ----------
def matmul(A, B, mod=10**18):
    n, m, p = len(A), len(B), len(B[0])
    C = [[0]*p for _ in range(n)]
    for i in range(n):
        for k in range(m):
            for j in range(p):
                C[i][j] = (C[i][j] + A[i][k]*B[k][j]) % mod
    return C

def matexp(M, power, mod=10**18):
    n = len(M)
    res = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    while power:
        if power & 1:
            res = matmul(res, M, mod)
        M = matmul(M, M, mod)
        power >>= 1
    return res
