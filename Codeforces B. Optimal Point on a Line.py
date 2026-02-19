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
arr = list_input()
arr.sort()
ans = arr[(n-1) // 2]
print(ans)
