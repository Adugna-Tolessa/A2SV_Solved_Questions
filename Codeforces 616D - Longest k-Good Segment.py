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

ans = [0,0,0]
store = defaultdict(int)
l = 0
for r in range(n):
    store[arr[r]] += 1
    while len(store) > k:
        store[arr[l]] -= 1
        if store[arr[l]] == 0:
            del store[arr[l]]
        l += 1
    ans = max([r - l + 1, l+1, r+1], ans)
print(*ans[1:])
