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
from collections import defaultdict
n, k = map_input()
arr = list_input()
ans = 0
store = defaultdict(int)
distinct = 0
l = 0
for r in range(n):
    if store[arr[r]] == 0:
        distinct += 1
    store[arr[r]] += 1
    while distinct > k:
        store[arr[l]] -= 1
        if store[arr[l]] == 0:
            distinct -= 1
        l += 1

    ans += (r-l + 1)
print(ans)
