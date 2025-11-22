# ---------- KMP ----------
def build_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp_search(text, pattern):
    lps = build_lps(pattern)
    res = []
    j = 0
    for i in range(len(text)):
        while j and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                res.append(i - j + 1)
                j = lps[j - 1]
    return res

# ---------- Z Algorithm ----------
def z_algorithm(s):
    z = [0] * len(s)
    l = r = 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

# ---------- ROLLING HASH ----------
class RollingHash:
    def __init__(self, s, base=911382, mod=10**9+7):
        self.mod = mod
        self.base = base
        n = len(s)
        self.pw = [1]*(n+1)
        self.h = [0]*(n+1)
        for i in range(n):
            self.h[i+1] = (self.h[i]*base + ord(s[i]))%mod
            self.pw[i+1] = (self.pw[i]*base)%mod

    def get_hash(self, l, r):
        return (self.h[r] - self.h[l]*self.pw[r-l]) % self.mod

# ---------- MANACHER (Longest Palindrome) ----------
def manacher(s):
    s = "#" + "#".join(s) + "#"
    n = len(s)
    p = [0] * n
    c = r = 0
    for i in range(n):
        mirror = 2*c - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and s[i+p[i]+1] == s[i-p[i]-1]:
            p[i] += 1
        if i + p[i] > r:
            c = i
            r = i + p[i]
    return p
