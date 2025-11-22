from itertools import permutations, combinations, product
from collections import defaultdict, deque, Counter
import bisect

# List operations
def sort_2d_list(matrix, key_column=0):
    """Sort 2D list by specified column"""
    return sorted(matrix, key=lambda x: x[key_column])

def reverse_list_in_place(arr):
    """Reverse list in place (modifies original list)"""
    arr.reverse()

def get_unique_sorted(arr):
    """Get unique elements from list while maintaining sorted order"""
    return sorted(set(arr))

def chunk_list(arr, chunk_size):
    """Split list into chunks of specified size"""
    return [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

# String operations
def reverse_string(s):
    """Reverse a string"""
    return s[::-1]

def count_vowels(s):
    """Count number of vowels in string"""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def is_anagram(s1, s2):
    """Check if two strings are anagrams"""
    return sorted(s1) == sorted(s2)

def string_to_char_frequency(s):
    """Convert string to character frequency dictionary"""
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Dictionary operations
def invert_dictionary(d):
    """Invert dictionary (swap keys and values)"""
    return {v: k for k, v in d.items()}

def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries (dict2 overwrites dict1 on conflict)"""
    return {**dict1, **dict2}

def sort_dictionary_by_key(d):
    """Sort dictionary by keys"""
    return dict(sorted(d.items()))

def sort_dictionary_by_value(d, reverse=False):
    """Sort dictionary by values"""
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))

# Set operations
def find_common_elements(list1, list2):
    """Find common elements between two lists"""
    return list(set(list1) & set(list2))

def find_unique_elements(list1, list2):
    """Find elements that are in one list but not the other"""
    return list(set(list1) ^ set(list2))

# Itertools helpers
def generate_permutations(arr, r=None):
    """Generate all permutations of arr of length r"""
    return list(permutations(arr, r))

def generate_combinations(arr, r):
    """Generate all combinations of arr of length r"""
    return list(combinations(arr, r))

def generate_cartesian_product(*arrays):
    """Generate Cartesian product of multiple arrays"""
    return list(product(*arrays))

# Bisect helpers for sorted lists
def insert_sorted(arr, x):
    """Insert element into sorted list while maintaining order"""
    bisect.insort(arr, x)

def find_range_in_sorted(arr, x):
    """Find the range of indices where x could be inserted to maintain order"""
    left = bisect.bisect_left(arr, x)
    right = bisect.bisect_right(arr, x)
    return left, right

# Type conversion helpers
def str_to_int_list(s, delimiter=' '):
    """Convert string of numbers to list of integers"""
    return list(map(int, s.split(delimiter)))

def int_list_to_str(arr, delimiter=' '):
    """Convert list of integers to string"""
    return delimiter.join(map(str, arr))

def matrix_to_str(matrix, row_delimiter='\n', col_delimiter=' '):
    """Convert 2D list to string representation"""
    return row_delimiter.join(col_delimiter.join(map(str, row)) for row in matrix)
