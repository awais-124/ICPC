# PYTHON DATA STRUCTURES BASICS - Lists, Tuples, Sets, Dictionaries

# ============ LISTS ============
# Ordered, mutable, allows duplicates, accessed by index
# Time: Access O(1), Insert/Delete O(n), Search O(n)

my_list = [1, 2, 3, 4, 5]

# ACCESS & MODIFY
my_list[0]           # First element: 1
my_list[-1]          # Last element: 5
my_list[1:4]         # Slice: [2, 3, 4]
my_list[::2]         # Every 2nd element: [1, 3, 5]
my_list[::-1]        # Reverse: [5, 4, 3, 2, 1]

# ADD/REMOVE
my_list.append(6)              # Add at end: [1,2,3,4,5,6]
my_list.extend([7, 8])         # Add multiple: [1,2,3,4,5,6,7,8]
my_list.insert(0, 0)           # Insert at index: [0,1,2,3,4,5,6,7,8]
my_list.remove(2)              # Remove first occurrence of 2
my_list.pop()                  # Remove last, return it
my_list.pop(2)                 # Remove at index 2
my_list.clear()                # Empty the list

# SEARCH & INFO
my_list = [1, 2, 3, 2, 4]
my_list.index(2)               # Find index of 2: 1 (first occurrence)
my_list.count(2)               # Count occurrences: 2
len(my_list)                   # Length: 5
2 in my_list                   # Check membership: True

# SORTING & REVERSING
my_list.sort()                 # Sort in place
my_list.sort(reverse=True)     # Sort descending
sorted(my_list)                # Returns new sorted list
my_list.reverse()              # Reverse in place

# COPYING
list_copy = my_list.copy()     # Shallow copy
list_copy = my_list[:]         # Slice copy
list_copy = list(my_list)      # Constructor copy


# ============ TUPLES ============
# Ordered, immutable, allows duplicates, faster than lists
# Use when you need immutable sequence or dict key

my_tuple = (1, 2, 3, 4, 5)

# ACCESS (same as list)
my_tuple[0]                    # 1
my_tuple[-1]                   # 5
my_tuple[1:3]                  # (2, 3)

# SEARCH & INFO
my_tuple.index(3)              # 2
my_tuple.count(2)              # 1
len(my_tuple)                  # 5
2 in my_tuple                  # True

# CREATE TUPLES
single = (42,)                 # Single element needs comma
empty = ()                     # Empty tuple
pair = 1, 2                    # Implicit tuple (without parentheses)

# UNPACKING
a, b, c = (1, 2, 3)          # Unpack into variables
a, *rest, z = (1, 2, 3, 4, 5) # a=1, rest=[2,3,4], z=5

# TUPLE AS DICT KEY
coord = (10, 20)
locations = {coord: "origin"}  # Can use tuple as key


# ============ SETS ============
# Unordered, mutable, NO duplicates, very fast membership testing
# Time: Add/Remove O(1), Contains O(1), but no indexing
# Use for: unique elements, mathematical set operations

my_set = {1, 2, 3, 4, 5}

# ADD/REMOVE
my_set.add(6)                  # Add one element
my_set.update([7, 8, 9])       # Add multiple
my_set.remove(3)               # Remove, raises KeyError if not found
my_set.discard(3)              # Remove, no error if not found
my_set.pop()                   # Remove arbitrary element
my_set.clear()                 # Empty set

# SEARCH & INFO
my_set = {1, 2, 3, 4, 5}
2 in my_set                    # True (fast!)
len(my_set)                    # 5

# SET OPERATIONS
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1 & set2                    # Intersection: {3}
set1 | set2                    # Union: {1, 2, 3, 4, 5}
set1 - set2                    # Difference: {1, 2}
set1 ^ set2                    # Symmetric difference: {1, 2, 4, 5}

set1 <= set2                   # Is subset
set1 >= set2                   # Is superset
set1.isdisjoint(set2)          # No common elements

# REMOVE DUPLICATES
numbers = [1, 2, 2, 3, 3, 3]
unique = list(set(numbers))    # [1, 2, 3] (order not guaranteed)


# ============ DICTIONARIES ============
# Unordered (in Python 3.7+, maintains insertion order), mutable
# Key-value pairs, keys must be hashable (immutable)
# Time: Access O(1), Insert/Delete O(1) average

my_dict = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
my_dict = {'name': 'Alice', 'age': 25, (1, 2): 'coordinate'}  # Keys can be various types

# ACCESS & MODIFY
my_dict['name']                # 'Alice'
my_dict.get('name')            # 'Alice' (safer, returns None if not found)
my_dict.get('age', 0)          # 25 (with default value)
my_dict['age'] = 26            # Update
my_dict['city'] = 'Boston'     # Create or update

# ADD/REMOVE
my_dict['email'] = 'alice@ex.com'  # Add new key
my_dict.update({'country': 'USA', 'age': 27})  # Merge/update multiple
del my_dict['city']            # Delete key
my_dict.pop('email')           # Remove and return value
my_dict.pop('missing', None)   # With default if not found
my_dict.clear()                # Empty dict

# SEARCH & INFO
my_dict = {'name': 'Alice', 'age': 25}
'name' in my_dict              # True (check key)
'Alice' in my_dict.values()    # Check value
len(my_dict)                   # 2

# ITERATION
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:            # Iterate keys
    print(key)

for value in my_dict.values(): # Iterate values
    print(value)

for key, value in my_dict.items():  # Iterate key-value pairs
    print(key, value)

# DICT METHODS
my_dict.keys()                 # dict_keys(['a', 'b', 'c'])
my_dict.values()               # dict_values([1, 2, 3])
my_dict.items()                # dict_items([('a',1), ('b',2)...])
my_dict.copy()                 # Shallow copy

# DEFAULT DICT (needs: from collections import defaultdict)
from collections import defaultdict
dd = defaultdict(list)         # Auto-create empty list for missing keys
dd['fruits'].append('apple')   # Works without initialization

# COUNTER (needs: from collections import Counter)
from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b', 'a'])  # {'a': 3, 'b': 2, 'c': 1}
counts.most_common(2)          # [('a', 3), ('b', 2)]


# ============ COMPARISON SUMMARY ============
"""
         | Ordered | Mutable | Duplicates | Indexing | Lookup | Use
---------|---------|---------|------------|----------|--------|----
List     | Yes     | Yes     | Yes        | Yes      | O(n)   | General purpose
Tuple    | Yes     | No      | Yes        | Yes      | O(n)   | Immutable, dict keys
Set      | No      | Yes     | No         | No       | O(1)   | Unique items, membership
Dict     | Yes*    | Yes     | Yes (vals) | By key   | O(1)   | Key-value storage

* Python 3.7+: Dict maintains insertion order
"""
