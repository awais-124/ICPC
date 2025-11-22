# STACKS & QUEUES - FIFO/LIFO data structures

# ============ STACK (Last In, First Out) ============
# Use for: DFS, expression evaluation, undo/redo, backtracking

# Simple implementation using list
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top"""
        self.items.append(item)

    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """View top item without removing"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Get size"""
        return len(self.items)


# Python's deque is faster for stack operations
from collections import deque

stack = deque()
stack.append(1)                                # Push 1
stack.append(2)                                # Push 2
stack.pop()                                    # 2 (pop from end)
stack[-1]                                      # 1 (peek)


# ============ STACK PROBLEMS ============

# 1. VALID PARENTHESES
def is_valid_parentheses(s):
    """Check if parentheses are balanced"""
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)

    return len(stack) == 0


# 2. NEXT GREATER ELEMENT
def next_greater_element(arr):
    """For each element, find next greater element to right"""
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result


# 3. EVALUATE POSTFIX EXPRESSION
def evaluate_postfix(expr):
    """Evaluate postfix expression like '5 3 +' = 8"""
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expr.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)
        else:
            stack.append(int(token))

    return stack[0] if stack else 0


# ============ QUEUE (First In, First Out) ============
# Use for: BFS, level-order traversal, scheduling, buffering

# Simple implementation using list
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add to back"""
        self.items.append(item)

    def dequeue(self):
        """Remove from front"""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        """View front item"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        """Check if empty"""
        return len(self.items) == 0

    def size(self):
        """Get size"""
        return len(self.items)


# Better: Use deque for O(1) operations
from collections import deque

queue = deque()
queue.append(1)                                # Enqueue 1
queue.append(2)                                # Enqueue 2
queue.popleft()                                # 1 (dequeue)
queue[0]                                       # 2 (front)


# ============ CIRCULAR QUEUE ============
# Fixed-size queue where end connects to beginning

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front_idx = 0
        self.rear_idx = -1
        self.size = 0

    def enqueue(self, item):
        """Add item"""
        if self.size == self.capacity:
            return False

        self.rear_idx = (self.rear_idx + 1) % self.capacity
        self.queue[self.rear_idx] = item
        self.size += 1
        return True

    def dequeue(self):
        """Remove item"""
        if self.size == 0:
            return None

        item = self.queue[self.front_idx]
        self.front_idx = (self.front_idx + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


# ============ PRIORITY QUEUE ============
# Use heapq for min-heap priority queue

import heapq

# Min heap (element with smallest priority comes out first)
pq = []
heapq.heappush(pq, (3, 'task3'))               # (priority, value)
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (2, 'task2'))

priority, task = heapq.heappop(pq)             # (1, 'task1')

# For max heap, negate priority
pq_max = []
heapq.heappush(pq_max, (-3, 'task3'))
heapq.heappush(pq_max, (-1, 'task1'))
priority, task = heapq.heappop(pq_max)         # (-3, 'task3')


# ============ DEQUE (Double-Ended Queue) ============
# Fast operations on both ends

from collections import deque

dq = deque([1, 2, 3])
dq.append(4)                                   # Add to right: [1, 2, 3, 4]
dq.appendleft(0)                               # Add to left: [0, 1, 2, 3, 4]
dq.pop()                                       # Remove from right: 4
dq.popleft()                                   # Remove from left: 0
dq.rotate(1)                                   # Rotate right: [3, 1, 2]
dq.rotate(-1)                                  # Rotate left: [1, 2, 3]


# ============ QUEUE PROBLEMS ============

# 1. IMPLEMENT STACK USING QUEUES
class StackUsingQueues:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        # Rotate to make newly added element at front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft() if not self.is_empty() else None

    def is_empty(self):
        return len(self.q) == 0


# 2. SLIDING WINDOW MAXIMUM
def sliding_window_maximum(arr, k):
    """Find max in each window of size k"""
    if not arr or k <= 0:
        return []

    from collections import deque
    dq = deque()
    result = []

    for i in range(len(arr)):
        # Remove elements outside window
        while dq and dq[0][1] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from back
        while dq and dq[-1][0] < arr[i]:
            dq.pop()

        dq.append((arr[i], i))

        if i >= k - 1:
            result.append(dq[0][0])

    return result


# 3. GENERATE NUMBERS WITH GIVEN DIGITS
def generate_numbers_with_digits(n, digits):
    """Generate first n numbers using only given digits"""
    from collections import deque

    queue = deque(digits)
    result = []

    while queue and len(result) < n:
        num = queue.popleft()
        result.append(num)

        for digit in digits:
            next_num = num * 10 + digit
            if len(str(next_num)) <= len(str(num)) + 1:
                queue.append(next_num)

    return result[:n]
