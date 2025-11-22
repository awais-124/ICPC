# PYTHON UTILITIES & TRICKS - Common patterns, built-in functions, list comprehensions

# ============ LIST COMPREHENSIONS ============
# Concise way to create lists - [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]              # [1, 4, 9, 16, 25]
even_squares = [x**2 for x in numbers if x % 2 == 0]  # [4, 16]
doubled = [x*2 for x in numbers]               # [2, 4, 6, 8, 10]

# Nested comprehension
matrix = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Flatten list
nested = [[1, 2, 3], [4, 5], [6]]
flat = [x for sublist in nested for x in sublist]  # [1, 2, 3, 4, 5, 6]

# Dict comprehension
squares_dict = {x: x**2 for x in range(5)}    # {0:0, 1:1, 2:4, 3:9, 4:16}
reversed_dict = {v: k for k, v in {'a': 1, 'b': 2}.items()}  # {1:'a', 2:'b'}

# Set comprehension
unique_squares = {x**2 for x in [1, 2, 2, 3, 3]}  # {1, 4, 9}

# Conditional expression in comprehension
result = ['even' if x % 2 == 0 else 'odd' for x in range(5)]  # ['even', 'odd', 'even', ...]


# ============ USEFUL BUILT-IN FUNCTIONS ============

# SUM - Add all elements
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)                           # 15
total_with_start = sum(numbers, 10)            # 25 (starts from 10)
sum_squares = sum(x**2 for x in numbers)       # 55 (with generator)

# MIN / MAX
min(numbers)                                   # 1
max(numbers)                                   # 5
min(numbers, key=lambda x: abs(x - 3))        # Element closest to 3

# MAP - Apply function to all elements
doubled = list(map(lambda x: x*2, numbers))   # [2, 4, 6, 8, 10]
strings = list(map(str, numbers))              # ['1', '2', '3', '4', '5']

# FILTER - Keep elements that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# ZIP - Pair elements from multiple iterables
letters = ['a', 'b', 'c']
paired = list(zip(numbers, letters))           # [(1,'a'), (2,'b'), (3,'c')]
# Unzip:
nums, chars = zip(*paired)                     # (1, 2, 3), ('a', 'b', 'c')

# ENUMERATE - Get index and value
for idx, val in enumerate(['a', 'b', 'c']):
    print(idx, val)                            # 0 a, 1 b, 2 c

# SORTED - Sort with custom key
words = ['apple', 'pie', 'a']
sorted(words, key=len)                         # ['a', 'pie', 'apple']
sorted(words, key=len, reverse=True)           # ['apple', 'pie', 'a']

# RANGE - Generate sequence
range(5)                                       # 0, 1, 2, 3, 4
range(2, 5)                                    # 2, 3, 4
range(0, 10, 2)                                # 0, 2, 4, 6, 8

# ANY / ALL - Check conditions
any([False, False, True])                      # True (at least one True)
all([True, True, True])                        # True (all True)
all([True, False, True])                       # False
any(x > 10 for x in [1, 2, 20])               # True

# REVERSED - Reverse sequence
list(reversed([1, 2, 3]))                      # [3, 2, 1]

# DIVMOD - Division and modulo together
q, r = divmod(17, 5)                           # q=3, r=2


# ============ STRING OPERATIONS ============

s = "hello world"

# FIND & SEARCH
s.find("world")                                # 6 (index, -1 if not found)
s.index("world")                               # 6 (index, raises error if not found)
s.count("o")                                   # 2

# CASE
s.upper()                                      # "HELLO WORLD"
s.lower()                                      # "hello world"
s.capitalize()                                 # "Hello world"
s.title()                                      # "Hello World"

# SPLIT & JOIN
words = s.split()                              # ['hello', 'world']
s.split('o')                                   # ['hell', ' w', 'rld']
' '.join(['hello', 'world'])                   # "hello world"

# STRIP
"  hello  ".strip()                            # "hello"
"  hello  ".lstrip()                           # "hello  "
"  hello  ".rstrip()                           # "  hello"

# REPLACE
s.replace("hello", "hi")                       # "hi world"
s.replace("o", "0", 1)                         # "hell0 world" (only first)

# CHECK
s.startswith("hello")                          # True
s.endswith("world")                            # True
s.isdigit()                                    # False
s.isalpha()                                    # False
s.isalnum()                                    # False

# FORMAT
"Hello, {0}!".format("Alice")                  # "Hello, Alice!"
f"Hello, {name}!"                              # f-string (Python 3.6+)


# ============ LAMBDA & FUNCTIONAL PROGRAMMING ============

# Lambda - Anonymous function
square = lambda x: x**2
square(5)                                      # 25

# With multiple arguments
add = lambda x, y: x + y
add(3, 4)                                      # 7

# Practical uses
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*2, numbers))   # [2, 4, 6, 8, 10]
result = list(filter(lambda x: x > 2, numbers))  # [3, 4, 5]


# ============ SORTING TRICKS ============

# Sort by multiple criteria
students = [('Alice', 25), ('Bob', 20), ('Charlie', 20)]
sorted(students, key=lambda x: (x[1], x[0]))   # Sort by age, then name

# Sort custom objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 25), Person('Bob', 20)]
sorted(people, key=lambda p: (p.age, p.name))

# Descending sort for some keys
# For multiple keys with mixed order: use tuple of (value, -value_if_reverse)
data = [(1, 'a'), (2, 'b'), (1, 'c')]
sorted(data, key=lambda x: (x[0], -ord(x[1])))


# ============ USEFUL IMPORTS FOR ICPC ============

from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
from math import gcd, lcm, comb, perm, factorial, sqrt, ceil, floor
from heapq import heappush, heappop, heapify
import bisect


# Counter - Count occurrences
from collections import Counter
s = "aabbbcccc"
counts = Counter(s)                            # Counter({'c': 4, 'b': 3, 'a': 2})
counts['a']                                    # 2
counts.most_common(2)                          # [('c', 4), ('b', 3)]

# defaultdict - Auto-initialize missing keys
from collections import defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')                   # No KeyError!
dd['fruits']                                   # ['apple']

# deque - Fast append/pop from both ends
from collections import deque
dq = deque([1, 2, 3])
dq.appendleft(0)                               # [0, 1, 2, 3]
dq.popleft()                                   # 0
dq.append(4)                                   # [1, 2, 3, 4]

# heapq - Priority queue (min heap by default)
import heapq
heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)                            # [1, 1, 4, 3, 5]
heapq.heappop(heap)                            # 1
heapq.heappush(heap, 2)                        # Add 2

# bisect - Binary search in sorted list
import bisect
arr = [1, 3, 5, 7]
bisect.bisect_left(arr, 5)                     # 2 (insert position for 5)
bisect.bisect_right(arr, 5)                    # 3

# itertools - Combinations & permutations
from itertools import combinations, permutations, product
list(combinations([1, 2, 3], 2))               # [(1,2), (1,3), (2,3)]
list(permutations([1, 2, 3], 2))               # [(1,2), (1,3), (2,1), ...]
list(product([0, 1], repeat=2))                # [(0,0), (0,1), (1,0), (1,1)]
