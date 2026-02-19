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

n = int_input()
arr = sorted(list_input())
count = 0
k = 1
for i in range(n):
    if arr[i] >= k:
        count += 1
        k += 1
print(count)
