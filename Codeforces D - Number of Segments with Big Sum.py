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

n, s = map_input()
arr = list_input()
store = 0
l = 0
ans = 0
for r in range(n):
    store += arr[r]
    while store >= s:
        ans += (n - r)
        store -= arr[l]
        l += 1
print(ans)
