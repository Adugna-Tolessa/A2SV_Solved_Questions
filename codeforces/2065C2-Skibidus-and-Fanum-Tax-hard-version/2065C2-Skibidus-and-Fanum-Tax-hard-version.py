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

import bisect

t = int_input()
for _ in range(t):
    n, m = map_input()
    a = list_input()
    b = list_input()
    b.sort()

    prev = -10 ** 18
    check = True

    for i in range(n):
        best = 10 ** 18
        if a[i] >= prev:
            best = a[i]

        need = prev + a[i]
        idx = bisect.bisect_left(b, need)

        if idx < m:
            val = b[idx] - a[i]
            if val >= prev:
                best = min(best, val)

        if best == 10 ** 18:
            check = False
            break

        prev = best

    print("YES" if check else "NO")