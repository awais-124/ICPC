from collections import deque, defaultdict, Counter
import heapq

class Stack:
    """LIFO Stack implementation using list"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return top item"""
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        """Return top item without removing"""
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return number of items in stack"""
        return len(self.items)

class Queue:
    """FIFO Queue implementation using deque"""
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return front item"""
        if not self.is_empty():
            return self.items.popleft()

    def front(self):
        """Return front item without removing"""
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return number of items in queue"""
        return len(self.items)

class PriorityQueue:
    """Min-heap implementation using heapq"""
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        """Add item with given priority"""
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """Remove and return item with smallest priority"""
        if not self.is_empty():
            return heapq.heappop(self.heap)[1]

    def peek(self):
        """Return item with smallest priority without removing"""
        if not self.is_empty():
            return self.heap[0][1]

    def is_empty(self):
        """Check if priority queue is empty"""
        return len(self.heap) == 0

    def size(self):
        """Return number of items in priority queue"""
        return len(self.heap)

def flatten_2d_list(matrix):
    """Flatten a 2D list into 1D list"""
    return [item for row in matrix for item in row]

def transpose_2d_list(matrix):
    """Transpose a 2D list (swap rows and columns)"""
    return [list(row) for row in zip(*matrix)]

def rotate_2d_list_90(matrix):
    """Rotate 2D list 90 degrees clockwise"""
    return [list(reversed(col)) for col in zip(*matrix)]

def create_2d_list(rows, cols, default=0):
    """Create a 2D list with given dimensions and default value"""
    return [[default] * cols for _ in range(rows)]

def list_to_frequency_dict(arr):
    """Convert list to frequency dictionary using Counter"""
    return dict(Counter(arr))

def merge_sorted_lists(lists):
    """Merge multiple sorted lists into one sorted list"""
    return list(heapq.merge(*lists))

def find_most_frequent(arr):
    """Find the most frequent element in a list"""
    if not arr:
        return None
    count = Counter(arr)
    return count.most_common(1)[0][0]
