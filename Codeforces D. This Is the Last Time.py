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
    n, k = map_input()
    store = []
    
    for tt in range(n):
        temp = list_input()
        store.append(temp)
    store.sort(key= lambda a: (a[2], a[0]))
    for casino in store:
        if k >= casino[0] and k <= casino[1]:
            k = max(k, casino[2])
    print(k)
