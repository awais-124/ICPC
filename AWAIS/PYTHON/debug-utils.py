import time
import random

def debug(*args, **kwargs):
    """Print debug information (useful during competitions)"""
    print("DEBUG:", *args, **kwargs)

def measure_time(func):
    """Decorator to measure function execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

def assert_equals(actual, expected, message=""):
    """Assert that actual equals expected (for quick testing)"""
    if actual != expected:
        print(f"❌ ASSERTION FAILED {message}: expected {expected}, got {actual}")
    else:
        print(f"✅ ASSERTION PASSED {message}")

def generate_test_case(min_val=0, max_val=100, size=10):
    """Generate random test case array"""
    return [random.randint(min_val, max_val) for _ in range(size)]

def print_2d_array(arr, name="Array"):
    """Pretty print 2D array"""
    print(f"{name}:")
    for row in arr:
        print(" ".join(f"{x:3}" for x in row))

def print_separator(length=50, char='='):
    """Print separator line for better output organization"""
    print(char * length)

def print_dict_pretty(d, name="Dictionary"):
    """Pretty print dictionary"""
    print(f"{name}:")
    for key, value in d.items():
        print(f"  {key}: {value}")

def compare_outputs(output1, output2):
    """Compare two outputs and highlight differences"""
    if output1 == output2:
        print("✅ Outputs are identical")
    else:
        print("❌ Outputs differ:")
        print(f"Output 1: {output1}")
        print(f"Output 2: {output2}")
