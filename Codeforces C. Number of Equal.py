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
n, m = map_input()
arr1 = list_input()
arr2 = list_input()

ans = 0
cnt1 = Counter(arr1)
cnt2 = Counter(arr2)
for key in cnt1:
    ans += cnt1[key] * cnt2[key]
print(ans)
