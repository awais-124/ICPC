# GRAPHS - Complete Reference for ICPC
# Includes adjacency list/matrix, BFS, DFS, Dijkstra, and more

# ============ GRAPH REPRESENTATIONS ============

# 1. Adjacency List (Most Common)
from collections import defaultdict, deque

class GraphAdjList:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight=1):
        """Add edge from u to v with optional weight"""
        self.graph[u].append((v, weight))
        # For undirected graph, also add: self.graph[v].append((u, weight))

    def display(self):
        for node in self.graph:
            print(f"{node}: {self.graph[node]}")


# 2. Adjacency Matrix
class GraphMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight=1):
        self.matrix[u][v] = weight
        # For undirected: self.matrix[v][u] = weight


# ============ GRAPH TRAVERSALS ============

# BFS (Breadth-First Search) - Level by level
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


# DFS (Depth-First Search) - Recursion
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


# DFS Iterative using stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor, _ in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


# ============ SHORTEST PATH ============

# Dijkstra's Algorithm (non-negative weights)
import heapq

def dijkstra(graph, start, end=None):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, node = heapq.heappop(pq)

        if curr_dist > distances[node]:
            continue

        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances


# ============ CYCLE DETECTION ============

# Undirected Graph - DFS
def has_cycle_undirected(graph, vertices):
    visited = [False] * vertices

    def dfs(v, parent):
        visited[v] = True
        for neighbor, _ in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    for i in range(vertices):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


# Directed Graph - DFS with color marking (White=0, Gray=1, Black=2)
def has_cycle_directed(graph, vertices):
    color = [0] * vertices

    def dfs(v):
        color[v] = 1
        for neighbor, _ in graph[v]:
            if color[neighbor] == 1:
                return True
            if color[neighbor] == 0:
                if dfs(neighbor):
                    return True
        color[v] = 2
        return False

    for i in range(vertices):
        if color[i] == 0:
            if dfs(i):
                return True
    return False


# ============ TOPOLOGICAL SORT ============

# Kahn's Algorithm (for DAG)
def topological_sort(graph, vertices):
    in_degree = [0] * vertices
    for u in graph:
        for v, _ in graph[u]:
            in_degree[v] += 1

    queue = deque([i for i in range(vertices) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result


# ============ CONNECTED COMPONENTS ============

def count_components(graph, vertices):
    visited = [False] * vertices
    count = 0

    def dfs(v):
        visited[v] = True
        for neighbor, _ in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)

    for i in range(vertices):
        if not visited[i]:
            dfs(i)
            count += 1

    return count
