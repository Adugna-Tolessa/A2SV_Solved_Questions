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
    s = input().strip()
    i = 0
    temp = set()
    
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i + 1]:
            i += 2
        else:
            temp.add(s[i])
            i += 1
    
    print("".join(sorted(temp)))
