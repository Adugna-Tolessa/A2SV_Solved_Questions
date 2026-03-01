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
from collections import defaultdict, Counter
t = int_input()
for _ in range(t):
    n, k = map_input()
    s = string_input()

    store = Counter(s[:k])
    ans = store["W"]
    for i in range(k, n):
        store[s[i]] += 1
        store[s[i - k]] -= 1
        ans = min(ans, store["W"])
    print(ans)

