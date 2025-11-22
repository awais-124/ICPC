from collections import deque, defaultdict
import heapq

# ---------- ADJ LIST BUILDER ----------
def build_graph(n, edges, directed=False):
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
        if not directed:
            g[v].append(u)
    return g

# ---------- BFS ----------
def bfs(start, graph):
    n = len(graph)
    dist = [-1] * n
    q = deque([start])
    dist[start] = 0

    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

# ---------- DFS ----------
def dfs(start, graph, visited=None):
    if visited is None:
        visited = [False] * len(graph)
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(v, graph, visited)
    return visited

# ---------- DIJKSTRA ----------
def dijkstra(start, graph):
    n = len(graph)
    dist = [10**18] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

# ---------- 0-1 BFS ----------
def zero_one_bfs(start, graph):
    n = len(graph)
    dist = [10**18] * n
    dist[start] = 0
    dq = deque([start])

    while dq:
        u = dq.popleft()
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if w == 1:
                    dq.append(v)
                else:
                    dq.appendleft(v)
    return dist

# ---------- TOPO SORT ----------
def topo_sort(graph):
    n = len(graph)
    indeg = [0] * n
    for u in range(n):
        for v in graph[u]:
            indeg[v] += 1

    q = deque([i for i in range(n) if indeg[i] == 0])
    res = []

    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return res

# ---------- DSU ----------
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.rank[a] < self.rank[b]:
            a, b = b, a
        self.p[b] = a
        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
        return True

# ---------- LCA (Binary Lifting) ----------
def build_lca(graph, root=0):
    n = len(graph)
    LOG = (n - 1).bit_length()
    parent = [[-1] * n for _ in range(LOG)]
    depth = [0] * n

    def dfs(u, p):
        for v in graph[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            parent[0][v] = u
            dfs(v, u)

    dfs(root, -1)

    for k in range(1, LOG):
        for i in range(n):
            if parent[k - 1][i] != -1:
                parent[k][i] = parent[k - 1][parent[k - 1][i]]

    def lca(a, b):
        if depth[a] < depth[b]:
            a, b = b, a
        diff = depth[a] - depth[b]
        for k in range(LOG):
            if diff & (1 << k):
                a = parent[k][a]

        if a == b:
            return a

        for k in reversed(range(LOG)):
            if parent[k][a] != parent[k][b]:
                a = parent[k][a]
                b = parent[k][b]

        return parent[0][a]

    return lca, depth
