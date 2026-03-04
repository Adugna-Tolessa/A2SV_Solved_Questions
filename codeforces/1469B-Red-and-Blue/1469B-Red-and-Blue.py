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
    r = list_input()
    m = int_input()
    b = list_input()
    r_pref = []
    r_max = 0
    b_max = 0
    b_pref = []
    for i in range(n):
        if r_pref:
            r_pref.append(r_pref[-1] + r[i])
            r_max = max(r_max, r_pref[-1])
        else:
            r_pref.append(r[i])
            r_max = max(r_max, r_pref[-1])
    for i in range(m):
        if b_pref:
            b_pref.append(b_pref[-1] + b[i])
            b_max = max(b_max, b_pref[-1])
        else:
            b_pref.append(b[i])
            b_max = max(b_max, b_pref[-1])
    print(r_max + b_max)