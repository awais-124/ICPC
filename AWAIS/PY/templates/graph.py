#!/usr/bin/env python3
# Graph template: adjacency list, BFS/DFS, weighted graph input

import sys
from collections import deque
from utils.fast_io import input, read_ints, read_int

def read_unweighted(n, m, one_indexed=True):
    edges = []
    for _ in range(m):
        u, v = read_ints()
        if one_indexed:
            u -= 1; v -= 1
        edges.append((u, v))
    return edges

def read_weighted(n, m, one_indexed=True):
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = read_ints()
        if one_indexed:
            u -= 1; v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    return g

def solve():
    n, m = read_ints()
    edges = read_unweighted(n, m)
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    # Example BFS from node 0
    dist = [-1]*n
    q = deque([0])
    dist[0] = 0
    while q:
        u = q.popleft()
        for v in g[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    print(dist)

if __name__ == "__main__":
    solve()
