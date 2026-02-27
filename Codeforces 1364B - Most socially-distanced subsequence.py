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

t = int_input()
for _ in range(t):
    n = int_input()
    p = list_input()
    
    ans = []
    for i in range(n):
        if i == 0 or i == n - 1:
            ans.append(p[i])
        else:
            if (p[i-1] < p[i]) != (p[i] < p[i+1]):
                ans.append(p[i])
    
    print(len(ans))
    print(*ans)
