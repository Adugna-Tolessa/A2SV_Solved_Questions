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
    a = list_input()
    b = list_input()
    # aa = []
    # bb = []
    ans = []

    i = 0
    while i < n - 1:
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            ans.append(["1", str(i + 1)])
            i = 0
            continue
        if b[i] > b[i + 1]:
            b[i], b[i + 1] = b[i + 1], b[i]
            ans.append(["2", str(i + 1)])
            i = 0
            continue
        i += 1
    j = 0
    
    while j < n:
        if a[j] > b[j]:
            a[j], b[j] = b[j], a[j]
            ans.append(["3", str(j + 1)])
        j += 1

    print(len(ans))
    for k in range(len(ans)):
        print(" ".join(ans[k]))
