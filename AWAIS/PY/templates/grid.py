#!/usr/bin/env python3
# Grid template: reading grid, 4-dir/8-dir moves, BFS example.

import sys
from collections import deque
from utils.fast_io import input, read_ints, read_int

DIR4 = [(1,0),(-1,0),(0,1),(0,-1)]
DIR8 = DIR4 + [(1,1),(1,-1),(-1,1),(-1,-1)]

def in_bounds(r, c, R, C):
    return 0 <= r < R and 0 <= c < C

def bfs_grid(sr, sc, grid, passable=lambda x: x == '.'):
    R, C = len(grid), len(grid[0])
    dist = [[-1]*C for _ in range(R)]
    q = deque()
    q.append((sr, sc))
    dist[sr][sc] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in DIR4:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc, R, C) and dist[nr][nc] == -1 and passable(grid[nr][nc]):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

def solve():
    R, C = read_ints()
    grid = [list(input().strip()) for _ in range(R)]
    sr, sc = read_ints()  # 0-indexed or 1-indexed depending on problem
    dist = bfs_grid(sr, sc, grid)
    # print distances (example)
    for row in dist:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    solve()
