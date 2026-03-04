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

n, k, q = map_input()

store = [0] * (200002)
pref = []
for _ in range(n):
    l, r = map_input()
    store[l] += 1
    store[r + 1] -= 1

for num in store:
    if pref:
        pref.append(pref[-1] + num)
    else:
        pref.append(num)

for i in range(1, 200002):
    pref[i] = 1 if pref[i] >= k else 0

for i in range(1, 200002):
    pref[i] = pref[i-1] + pref[i]


for _ in range(q):
    a, b = map_input()
    cnt = 0
    print(pref[b]-pref[a-1])
    # for j in range(a, b + 1):
    #     if pref[j] >= k:
    #         cnt += 1
    # print(cnt)