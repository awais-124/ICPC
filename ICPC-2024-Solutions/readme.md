# ICPC 2024 Asia Topi - Solutions Guide

## 📊 Quick Problem Overview

| Problem | Title                | Algorithm                           | Time Limit | Status |
| ------- | -------------------- | ----------------------------------- | ---------- | ------ |
| 01      | Circuit Design       | Graph Theory (Triangle Counting)    | 18s        | ✅     |
| 02      | Car Washing          | Dynamic Programming (Assembly Line) | 1s         | ✅     |
| 03      | Stock Trader         | DP (Max Profit K Transactions)      | 1s         | ✅     |
| 04      | Calligraphy Crisis   | String Algorithms (Anagrams)        | 6s         | ✅     |
| 05      | BioDiversity Scan    | Combinatorics (Stars & Bars)        | 1s         | ✅     |
| 06      | Event Management     | String Parsing & Sequence           | 1s         | ✅     |
| 07      | Electoral Boundaries | Graph Coloring (Bipartite Check)    | 1s         | ✅     |
| 08      | Optimized Path       | Dijkstra + Number Theory (Primes)   | 1s         | ✅     |
| 09      | Ancestral Queries    | Binary Lifting (LCA)                | 1s         | ✅     |

---

## 🔍 Detailed Solution Breakdown

### **Problem 01: Circuit Design**

**Input:** Graph with N nodes, M edges
**Output:** Count of triangles in graph

**Approach:**

- For each edge (u,v), find common neighbors
- Common neighbors form triangles with (u,v)
- Count each triangle once by checking u < v

**Key Insight:** If nodes u and v both connect to w, then (u,v,w) form a triangle

**Time Complexity:** O(N \* deg²) where deg = average degree

---

### **Problem 02: Car Washing**

**Input:** 2 lanes with N stations each, processing times, switch costs
**Output:** Minimum total time

**Approach:** DP with states:

- `dp[i][0]` = min time to reach station i in lane 1
- `dp[i][1]` = min time to reach station i in lane 2

**Recurrence:**

```
dp[i][0] = min(dp[i-1][0] + w1[i], dp[i-1][1] + s2[i-1] + w1[i])
dp[i][1] = min(dp[i-1][1] + w2[i], dp[i-1][0] + s1[i-1] + w2[i])
```

**Key Insight:** Classic assembly line scheduling problem

---

### **Problem 03: Stock Trader**

**Input:** Stock prices array, max K transactions
**Output:** Maximum profit

**Approach:** DP with transaction limit

- If K ≥ N/2: unlimited transactions (greedy)
- Else: `buy[j]` = max profit with j transactions holding stock
  `sell[j]` = max profit with j transactions not holding stock

**Key Insight:** Either do unlimited or limited transactions

---

### **Problem 04: Calligraphy Crisis**

**Input:** N calligraphy pieces, Q query words
**Output:** For each query, count pieces with anagram prefix

**Approach:**

- For each query, check all calligraphy pieces
- For each piece, check if any prefix is anagram of query
- Count matches

**Key Insight:** Use sorted strings to check anagrams

---

### **Problem 05: BioDiversity Scan**

**Input:** N insect types, T total count, M minimum per type
**Output:** Number of ways to partition

**Approach:** Stars and Bars combinatorics

- Each insect must have ≥ M count
- Reduce problem: subtract N*M from total → `new_t = T - N*M`
- Answer = C(new_t + N - 1, N - 1)

**Key Insight:** This is composition of new_t into N parts

---

### **Problem 06: Event Management**

**Input:** Event code string
**Output:** Longest unique sequence + counts

**Approach:**

1. Parse string into 3-char event codes
2. Check validity: must be [A-G][0-9][0-9]
3. For each starting position, find longest unique sequence
4. Choose lexicographically smallest if tie
5. Count event types in sequence

**Key Insight:** Longest substring with unique elements

---

### **Problem 07: Electoral Boundaries**

**Input:** N blocks, W roads connecting them
**Output:** Maximum number of polling districts

**Approach:** Graph bipartiteness check

- Color graph using BFS (0 and 1 coloring)
- If bipartite: answer = 2 (two districts)
- If not bipartite: answer = -1 (impossible)

**Special Case:** For more connected components or specific layouts, may need different approach

---

### **Problem 08: Optimized Path**

**Input:** N towns, R roads with distances, exit point E, token T
**Output:** Shortest distance + sum of 3 largest primes < T

**Approach:**

- Use Dijkstra from town 1 to town E
- Find 3 largest prime numbers less than T
- Sum those primes

**Key Insight:** Combination of shortest path + number theory

---

### **Problem 09: Ancestral Queries**

**Input:** Family tree (parent-child), Q queries (u, k)
**Output:** For each query, find kth ancestor

**Approach:** Binary Lifting

- Preprocess: `lift[u][j]` = 2^j-th ancestor of u
- Query: decompose k into powers of 2, jump accordingly
- O(log N) per query after O(N log N) preprocessing

**Key Insight:** Fast ancestor queries in trees

---

## 🛠️ Common Patterns Used

| Pattern           | Problems | File            |
| ----------------- | -------- | --------------- |
| DP                | 02, 03   | Python_DAA, CPP |
| Graph Theory      | 01, 07   | Python_DAA, CPP |
| String Algorithms | 04, 06   | Python_DAA, CPP |
| Combinatorics     | 05       | Python_DAA, CPP |
| Number Theory     | 08       | Python_DAA, CPP |
| Tree Algorithms   | 09       | Python_DAA, CPP |
| Two Pointers      | Many     | Python_DAA      |

---

## 📋 File Structure

### **Python_DAA_Approaches_Complete.py**

Contains all 14 algorithmic approaches:

1. Two Pointer
2. Sliding Window
3. Dynamic Programming
4. LCS
5. LIS
6. Edit Distance
7. Coin Change
8. Matrix Chain
9. Binary Search
10. Greedy
11. Memoization
12. Graph Algorithms
13. Divide & Conquer
14. Backtracking

### **ICPC_Problems_Solutions_Python.py**

Contains all 9 problem solutions with proper input/output handling

### **ICPC_Problems_Solutions_CPP.cpp**

Contains all 9 problem solutions with optimizations

---

## 🚀 How to Use

### For Python:

```python
# Uncomment the problem in main section
if __name__ == "__main__":
    problem01()  # or any problem number
```

### For C++:

```cpp
// Uncomment in main():
int main() {
    // problem01();
    return 0;
}
```

---

## ⚡ Optimization Tips

### Python:

- Use `from math import comb` for combinations
- Use sets for O(1) lookups
- Use `defaultdict` for graph representations

### C++:

- Use `priority_queue` with custom comparator
- Use bitwise operations for speed
- Pre-allocate vectors/arrays

---

## 🎯 Complexity Analysis

| Problem | Time             | Space    | Notes                |
| ------- | ---------------- | -------- | -------------------- |
| 01      | O(M²)            | O(N)     | Triangle enumeration |
| 02      | O(N)             | O(N)     | DP tabulation        |
| 03      | O(NK)            | O(K)     | Transaction DP       |
| 04      | O(N*Q*L²)        | O(1)     | String sorting       |
| 05      | O(N²)            | O(N²)    | Binomial coeff       |
| 06      | O(L²)            | O(L)     | Substring search     |
| 07      | O(N+W)           | O(N)     | Graph coloring       |
| 08      | O((N+R)logN)     | O(N)     | Dijkstra + primes    |
| 09      | O(NlogN + QlogN) | O(NlogN) | Binary lifting       |

---

## 🧪 Testing Recommendations

1. **Problem 01:** Test with small graphs (triangles)
2. **Problem 02:** Test with equal lane costs
3. **Problem 03:** Test with unlimited (k=0) and limited transactions
4. **Problem 04:** Test with overlapping anagrams
5. **Problem 05:** Test edge cases (N=0, T < N\*M)
6. **Problem 06:** Test invalid codes early in string
7. **Problem 07:** Test with cycles (bipartite check)
8. **Problem 08:** Test with disconnected nodes
9. **Problem 09:** Test with k > depth (should return -1)

---

## 📝 Notes

- All solutions handle multiple test cases
- Python and C++ produce identical output
- Code is optimized for both readability and speed
- Print statements match exact format requirements
- Edge cases are handled (overflow, disconnected, empty inputs)
