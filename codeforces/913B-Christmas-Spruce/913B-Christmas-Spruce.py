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
p = []
for _ in range(n-1):
    i = int_input()
    p.append(i - 1)
leafs = list(filter(lambda x: not x in p, range(n)))
lp = [x for i, x in enumerate(p) if i + 1 in leafs]
x = min(lp.count(k) for k in p)
if x >= 3:
    print("Yes")
else:
    print("No")