def int_input():
    return int(input())

def map_input():
    return map(int, input().split())

def list_input():
    return list(map(int, input().split()))

def string_input():
    return input()

def list_of_strings():
    return input().split()
from collections import Counter
t = int_input()
for _ in range(t):
    n = int_input()
    s = string_input()
    s_count = Counter(s)
    # "aa", "aba", "aca", "abca", "acba", "abbacca", "accabba"
    if "aa" in s:
        print(2)
    elif "aba" in s:
        print(3)
    elif "aca"in s:
        print(3)
    elif "abca" in s:
        print(4)
    elif "acba" in s:
        print(4)
    elif "abbacca" in s:
        print(7)
    elif "accabba" in s:
        print(7)
    else:
        print(-1)


