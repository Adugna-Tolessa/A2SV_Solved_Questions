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
t = int_input()
for _ in range(t):
    n = int_input()
    a = string_input()
    b = string_input()
    a += '0'
    b += '0'
    
    cnt = 0
    
    for i in range(n):
        cnt += (a[i] == '1') - (a[i] == '0')
        
        if ((a[i] == b[i]) != (a[i + 1] == b[i + 1])) and cnt != 0:
            print("NO")
            break
    else:
        print("YES")
