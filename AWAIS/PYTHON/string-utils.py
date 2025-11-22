def is_palindrome(s):
    return s == s[::-1]

def kmp_search(pattern, text):
    """Knuth-Morris-Pratt string matching algorithm"""
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

def z_algorithm(s):
    """Z-algorithm for string matching"""
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def manacher(s):
    """Manacher's algorithm for longest palindromic substring"""
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c, r = 0, 0
    for i in range(n):
        if i < r:
            p[i] = min(r - i, p[2 * c - i])
        while (i + p[i] + 1 < n and i - p[i] - 1 >= 0 and
               t[i + p[i] + 1] == t[i - p[i] - 1]):
            p[i] += 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    return p
