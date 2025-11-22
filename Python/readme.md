# ICPC Quick Reference - File Guide

## Quick Navigation

| Need                                             | Go To       |
| ------------------------------------------------ | ----------- |
| **Graphs** (BFS, DFS, Dijkstra, cycles)          | **File 01** |
| **Trees** (traversals, BST, LCA)                 | **File 02** |
| **Combinations/Permutations**                    | **File 03** |
| **Linked Lists** (singly/doubly)                 | **File 04** |
| **DP/Greedy** (knapsack, coin change, LCS)       | **File 05** |
| **Lists, Tuples, Sets, Dicts**                   | **File 06** |
| **Math** (GCD, primes, modular, bits)            | **File 07** |
| **Python tricks** (comprehensions, map/filter)   | **File 08** |
| **Stack/Queue** (implementations, problems)      | **File 09** |
| **Sorting/Searching** (binary search, all sorts) | **File 10** |

---

## File Breakdown

### **File 01: Graphs_Complete_Reference.py**

- Graph representations (adjacency list/matrix)
- BFS (level-by-level), DFS (recursive & iterative)
- Dijkstra's shortest path
- Cycle detection (directed & undirected)
- Topological sort (Kahn's algorithm)
- Connected components

### **File 02: Trees_Complete_Reference.py**

- Tree node class & construction
- Traversals: inorder, preorder, postorder, level-order
- Height, count nodes, sum, max value
- Balanced tree check
- BST search, min, max, delete
- Lowest Common Ancestor (LCA)
- Path finding from root

### **File 03: Combinatorics_Reference.py**

- C(n,r) combinations without repetition
- Combinations with repetition
- P(n,r) permutations without repetition
- Permutations with repetition (n^r)
- Multiset permutations (with duplicates)
- Pascal's triangle
- Modular arithmetic (for large factorials)

### **File 04: LinkedList_Complete_Reference.py**

- Node classes (singly & doubly)
- Singly linked list: insert/delete/search/reverse
- Doubly linked list: insert/delete/reverse
- Length, traverse, to_list conversion
- Middle finding (slow/fast pointer)
- Palindrome check, cycle detection

### **File 05: DP_and_Greedy_Reference.py**

- Fibonacci (recursive, memoization, tabulation)
- 0/1 Knapsack
- Longest Common Subsequence (LCS)
- Coin change (minimum & combinations)
- Longest Increasing Subsequence (LIS)
- Edit distance (Levenshtein)
- Matrix chain multiplication
- Activity selection, fractional knapsack
- Huffman coding, interval scheduling

### **File 06: Data_Structures_Basics.py**

- **Lists**: append, extend, insert, remove, pop, sort, slice
- **Tuples**: indexing, unpacking, as dict keys
- **Sets**: add, remove, union, intersection, difference
- **Dicts**: get, set, keys, values, items, pop
- defaultdict, Counter usage
- Comparison table (when to use what)

### **File 07: Math_Algorithms_Reference.py**

- GCD & LCM (Euclidean algorithm)
- Prime checking, Sieve of Eratosthenes
- Prime factorization
- Modular arithmetic (add, subtract, multiply, power)
- Modular inverse & extended GCD
- Euler's totient
- Digit operations (sum, root, count)
- Fast power, power of 2 checks
- Binary search in sorted arrays
- Bit manipulation (set, clear, toggle, count bits)

### **File 08: Python_Utils_and_Tricks.py**

- **List comprehensions**: basic, nested, conditional
- **Dict/Set comprehensions**
- **Built-in functions**: sum, min, max, map, filter, zip, enumerate, sorted, any, all, reversed, divmod
- **String operations**: find, case, split, join, strip, replace, startswith, isdigit
- **Lambda functions** & functional programming
- **Sorting tricks** (custom keys, multiple criteria)
- **Important imports**: Counter, defaultdict, deque, combinations, permutations, heapq, bisect

### **File 09: Queue_Stack_Reference.py**

- Stack class & deque usage
- Valid parentheses check
- Next greater element
- Postfix expression evaluation
- Queue class & deque usage
- Circular queue implementation
- Priority queue (min/max heap)
- Deque operations & rotate
- Stack using queues
- Sliding window maximum
- Number generation with digits

### **File 10: Sorting_and_Searching_Reference.py**

- Python's built-in sort & sorted()
- Binary search (exact, leftmost, rightmost)
- bisect module usage
- Merge sort (stable, O(n log n))
- Quick sort (in-place & simple versions)
- Selection algorithms (kth smallest)
- Counting sort (O(n + k))
- Radix sort (O(d\*n))
- Linear search, exponential search
- Two-pointers technique
- Sorting stability

---

## Common Patterns Quick Access

| Problem Type    | File | Key Functions                                       |
| --------------- | ---- | --------------------------------------------------- |
| Graph traversal | 01   | bfs(), dfs_recursive(), dfs_iterative()             |
| Shortest path   | 01   | dijkstra()                                          |
| Tree traversal  | 02   | inorder(), preorder(), postorder(), level_order()   |
| Permutations    | 03   | get_permutations(), permutations_with_rep()         |
| Combinations    | 03   | get_combinations(), combinations_with_rep()         |
| DP knapsack     | 05   | knapsack_01()                                       |
| DP strings      | 05   | lcs(), edit_distance()                              |
| Primes          | 07   | is_prime(), sieve_of_eratosthenes()                 |
| Modular math    | 07   | mod_power(), mod_inverse()                          |
| Stacks          | 09   | is_valid_parentheses(), next_greater_element()      |
| Queues          | 09   | sliding_window_maximum()                            |
| Search          | 10   | binary_search_leftmost(), binary_search_rightmost() |
| Sort            | 10   | merge_sort(), quick_sort()                          |

---

## Tips for Using During Contest

1. **Ctrl+F (Find)** to search for exact function names
2. **Check time complexity** comments for which algorithm to use
3. **Copy entire class** if you need a data structure
4. **Modify to fit** input/output format of specific problem
5. **Use Python built-ins** first (sorted, set operations, Counter)
6. **Keep MOD = 10^9+7** handy for modular arithmetic problems

**Good luck! 🚀**
