import sys
import math

def get_int():
    return int(sys.stdin.readline().strip())

def get_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def get_float():
    return float(sys.stdin.readline().strip())

def get_floats():
    return list(map(float, sys.stdin.readline().strip().split()))

def get_string():
    return sys.stdin.readline().strip()

def get_strings():
    return sys.stdin.readline().strip().split()

# Fast output (useful when output is large)
def print_array(arr, sep=' '):
    print(sep.join(map(str, arr)))

def print_matrix(matrix, sep=' '):
    for row in matrix:
        print_array(row, sep)
