def is_power_of_two(n):
    """Check if number is power of two using bit manipulation"""
    return n > 0 and (n & (n - 1)) == 0

def count_set_bits(n):
    """Count number of 1 bits in number (Brian Kernighan's algorithm)"""
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count

def get_bit(n, pos):
    """Get bit at specific position (0-indexed from right)"""
    return (n >> pos) & 1

def set_bit(n, pos):
    """Set bit at specific position to 1"""
    return n | (1 << pos)

def clear_bit(n, pos):
    """Set bit at specific position to 0"""
    return n & ~(1 << pos)

def toggle_bit(n, pos):
    """Toggle bit at specific position (0->1, 1->0)"""
    return n ^ (1 << pos)

def lowest_set_bit(n):
    """Get position of lowest set bit (rightmost 1)"""
    return (n & -n).bit_length() - 1

def highest_set_bit(n):
    """Get position of highest set bit"""
    return n.bit_length() - 1 if n > 0 else -1

def is_even(n):
    """Check if number is even using bit operation"""
    return (n & 1) == 0

def is_odd(n):
    """Check if number is odd using bit operation"""
    return (n & 1) == 1

def multiply_by_power_of_two(n, power):
    """Multiply number by 2^power using left shift"""
    return n << power

def divide_by_power_of_two(n, power):
    """Divide number by 2^power using right shift"""
    return n >> power

def swap_numbers(a, b):
    """Swap two numbers without temporary variable using XOR"""
    a ^= b
    b ^= a
    a ^= b
    return a, b

def generate_subsets(arr):
    """Generate all subsets of array using bitmask"""
    n = len(arr)
    subsets = []
    for mask in range(1 << n):
        subset = [arr[i] for i in range(n) if (mask >> i) & 1]
        subsets.append(subset)
    return subsets
