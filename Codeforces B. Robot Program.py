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
    n, x, k = map_input()
    s = string_input()   
    for i in range(n):
        if s[i] == 'L':
            x -= 1
        else:
            x += 1
        k -= 1
        if x == 0:
            break

    ans = 0
    if x == 0:
        ans = 1
        for i in range(n):
            if s[i] == 'L':
                x -= 1
            else:
                x += 1
            if x == 0:
                ans += k // (i + 1)
                break

    print(ans)
