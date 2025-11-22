# ============ ICPC 2024 ASIA TOPI - PYTHON SOLUTIONS ============

# ============ PROBLEM 01: CIRCUIT DESIGN - Subgraph Pattern Counting ============

def count_triangles(n, edges):
    """Count all triangles (3-node subgraphs) in undirected graph"""
    # Build adjacency list
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    count = 0
    # For each edge (u,v), count common neighbors
    for u in range(n):
        for v in adj[u]:
            if u < v:  # Avoid counting same triangle 3 times
                common = adj[u] & adj[v]
                count += len(common)

    # Each triangle counted once now
    return count


def problem01():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = count_triangles(n, edges)
    print(result)


# ============ PROBLEM 02: CAR WASHING - Assembly Line Scheduling (DP) ============

def car_washing(n, e1, e2, w1, w2, s1, s2, x1, x2):
    """Minimum time to wash car on 2 parallel lanes with switching"""
    # dp[i][j] = min time to reach station i on lane j (0=lane1, 1=lane2)
    dp = [[0] * 2 for _ in range(n)]

    # Station 1
    dp[0][0] = e1 + w1[0]
    dp[0][1] = e2 + w2[0]

    # Fill rest of stations
    for i in range(1, n):
        # Reach station i, lane 1: either from lane 1 or switch from lane 2
        dp[i][0] = min(dp[i-1][0] + w1[i],      # Stay in lane 1
                      dp[i-1][1] + s2[i-1] + w1[i])  # Switch from lane 2

        # Reach station i, lane 2: either from lane 2 or switch from lane 1
        dp[i][1] = min(dp[i-1][1] + w2[i],      # Stay in lane 2
                      dp[i-1][0] + s1[i-1] + w2[i])  # Switch from lane 1

    # Exit from either lane
    result = min(dp[n-1][0] + x1, dp[n-1][1] + x2)
    return result


def problem02():
    t = int(input())
    for _ in range(t):
        n = int(input())
        e1, e2 = map(int, input().split())
        w1 = list(map(int, input().split()))
        w2 = list(map(int, input().split()))
        s1 = list(map(int, input().split()))
        s2 = list(map(int, input().split()))
        x1, x2 = map(int, input().split())

        result = car_washing(n, e1, e2, w1, w2, s1, s2, x1, x2)
        print(result)


# ============ PROBLEM 03: STOCK TRADER - Max Profit with K Transactions (DP) ============

def max_profit_k_transactions(prices, k):
    """Maximum profit with at most k transactions"""
    if not prices or k == 0:
        return 0

    n = len(prices)
    # If k >= n/2, we can do unlimited transactions
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            profit += max(0, prices[i] - prices[i-1])
        return profit

    # buy[i] = max profit after at most i transactions with stock in hand
    # sell[i] = max profit after at most i transactions with no stock
    buy = [-prices[0]] * (k + 1)
    sell = [0] * (k + 1)

    for i in range(1, n):
        for j in range(k, 0, -1):
            sell[j] = max(sell[j], buy[j] + prices[i])
            buy[j] = max(buy[j], sell[j-1] - prices[i])

    return sell[k]


def problem03():
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        prices = list(map(int, input().split()))

        result = max_profit_k_transactions(prices, k)
        print(result)


# ============ PROBLEM 04: CALLIGRAPHY CRISIS - Anagram Prefix Finding ============

def find_anagram_prefixes(calligraphies, queries):
    """Find calligraphies with anagram prefix for each query"""
    results = []

    for query in queries:
        count = 0
        query_sorted = sorted(query)
        query_len = len(query)

        for calli in calligraphies:
            # Check all prefixes of calligraphy
            for end in range(query_len, len(calli) + 1):
                prefix = calli[:end]
                if len(prefix) >= query_len:
                    if sorted(prefix[:query_len]) == query_sorted:
                        count += 1
                        break  # Found in this calligraphy, move to next

        results.append(count if count > 0 else -1)

    return results


def problem04():
    n = int(input())
    calligraphies = []
    for _ in range(n):
        calligraphies.append(input().strip())

    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(input().strip())

    results = find_anagram_prefixes(calligraphies, queries)
    for r in results:
        print(r)


# ============ PROBLEM 05: BIODIVERSITY SCAN - Partitions with Minimum ============

def count_partitions(n, t, m):
    """Count ways to partition t into n parts, each >= m"""
    if n == 0:
        return 1 if t == 0 else 0
    if t < n * m:
        return 0

    # Transform: each part starts with m, so reduce by n*m
    new_t = t - n * m

    # Now count partitions of new_t into n non-negative parts
    # This is stars and bars: C(new_t + n - 1, n - 1)
    from math import comb
    return comb(new_t + n - 1, n - 1)


def problem05():
    k = int(input())
    for _ in range(k):
        n, t, m = map(int, input().split())
        result = count_partitions(n, t, m)
        print(result)


# ============ PROBLEM 06: EVENT MANAGEMENT - Longest Unique Subsequence ============

def is_valid_code(code):
    """Check if event code is valid"""
    if len(code) != 3:
        return False
    if code[0] not in 'ABCDEFG':
        return False
    if not code[1:].isdigit():
        return False
    return True


def problem06():
    t = int(input())
    for _ in range(t):
        s = input().strip()

        # Parse event codes (each code is 3 chars)
        codes = []
        invalid_code = None

        for i in range(0, len(s), 3):
            code = s[i:i+3]
            if not is_valid_code(code):
                invalid_code = code
                break
            codes.append(code)

        if invalid_code:
            print(f"-1 {invalid_code}")
            continue

        # Find longest unique subsequence
        max_length = 0
        best_sequence = []

        for start in range(len(codes)):
            seen = set()
            sequence = []
            for i in range(start, len(codes)):
                if codes[i] not in seen:
                    seen.add(codes[i])
                    sequence.append(codes[i])
                else:
                    break

            if len(sequence) > max_length or (len(sequence) == max_length and
                (not best_sequence or sequence[0] < best_sequence[0])):
                max_length = len(sequence)
                best_sequence = sequence

        # Count event types
        category_count = {}
        category_names = {'A': 'Competitions', 'B': 'Entertainment',
                         'C': 'Social Gatherings', 'D': 'Dinners',
                         'E': 'Processions', 'F': 'Training Workshops', 'G': 'Exams'}

        for code in best_sequence:
            cat = code[0]
            category_count[cat] = category_count.get(cat, 0) + 1

        # Output
        print(max_length, ' '.join(best_sequence))
        count_str = ' '.join([f"{count} {category_names[cat]}"
                             for cat, count in sorted(category_count.items())])
        print(count_str)


# ============ PROBLEM 07: ELECTORAL BOUNDARIES - Graph Coloring ============

def max_polling_districts(n, edges):
    """Maximum number of consecutive districts (graph 2-coloring + BFS levels)"""
    from collections import defaultdict, deque

    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Check if bipartite using BFS coloring
    color = [-1] * (n + 1)
    is_bipartite = True
    max_level = 0

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        queue = deque([start])
        color[start] = 0
        level = 0

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    is_bipartite = False
                    break

        max_level = max(max_level, max(color[1:n+1]) + 1)

    if not is_bipartite:
        return -1

    return max_level


def problem07():
    t = int(input())
    for _ in range(t):
        n = int(input())
        w = int(input())
        edges = []
        for _ in range(w):
            u, v = map(int, input().split())
            edges.append((u, v))

        result = max_polling_districts(n, edges)
        print(result)


# ============ PROBLEM 08: OPTIMIZED PATH COUNTRY - Shortest Path + Prime Sum ============

def dijkstra_shortest_path(n, edges, start, end):
    """Find shortest path from start to end"""
    import heapq

    adj = [[] for _ in range(n + 1)]
    for u, v, d in edges:
        adj[u].append((v, d))
        adj[v].append((u, d))

    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist[end] if dist[end] != float('inf') else 2147483647


def three_largest_primes_below(n):
    """Get sum of three largest primes below n"""
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    primes = []
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            primes.append(i)
            if len(primes) == 3:
                break

    return sum(primes) if len(primes) >= 3 else sum(primes)


def problem08():
    n, r, e, t = map(int, input().split())
    edges = []
    for _ in range(r):
        u, v, d = map(int, input().split())
        edges.append((u, v, d))

    distance = dijkstra_shortest_path(n, edges, 1, e)
    token_value = three_largest_primes_below(t)

    print(distance, token_value)


# ============ PROBLEM 09: ANCESTRAL QUERIES - Kth Ancestor using Binary Lifting ============

def kth_ancestor(n, parent_map, q, queries, root):
    """Find kth ancestor for each query using preprocessing"""
    # Build tree structure
    children = [[] for _ in range(n + 1)]
    for child, parent in parent_map.items():
        children[parent].append(child)

    # Binary lifting preprocessing
    LOG = 20
    lift = [[0] * LOG for _ in range(n + 1)]
    depth = [0] * (n + 1)

    # BFS to build tree and calculate depth
    from collections import deque
    queue = deque([root])
    visited = [False] * (n + 1)
    visited[root] = True

    while queue:
        u = queue.popleft()
        for v in children[u]:
            if not visited[v]:
                visited[v] = True
                depth[v] = depth[u] + 1
                lift[v][0] = u
                queue.append(v)

    # Build lift table
    for j in range(1, LOG):
        for i in range(1, n + 1):
            if lift[i][j-1] != 0:
                lift[i][j] = lift[lift[i][j-1]][j-1]

    # Answer queries
    results = []
    for u, k in queries:
        current = u
        for j in range(LOG):
            if k & (1 << j):
                current = lift[current][j]
                if current == 0:
                    break

        results.append(current if current != 0 else -1)

    return results


def problem09():
    t = int(input())
    for _ in range(t):
        n, q, r = map(int, input().split())

        parent_map = {}
        for _ in range(n - 1):
            parent, child = map(int, input().split())
            parent_map[child] = parent

        queries = []
        for _ in range(q):
            u, k = map(int, input().split())
            queries.append((u, k))

        results = kth_ancestor(n, parent_map, q, queries, r)
        for res in results:
            print(res)


# ============ MAIN EXECUTOR ============

if __name__ == "__main__":
    # Uncomment the problem you want to test
    # problem01()
    # problem02()
    # problem03()
    # problem04()
    # problem05()
    # problem06()
    # problem07()
    # problem08()
    # problem09()
    pass
