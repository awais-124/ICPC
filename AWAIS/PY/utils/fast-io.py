import sys
import threading

def input():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(input())

def read_ints():
    return list(map(int, input().split()))

def read_str():
    return input()

def read_list():
    return input().split()

def fast_output(s):
    sys.stdout.write(str(s))

# Optional threaded main wrapper to avoid recursion limit problems in contests
def run_main(main_func):
    threading.Thread(target=main_func).start()
