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

from collections import Counter
from collections import Counter
t = int_input()
for _ in range(t):
    n, l, r = map_input()
    socks = list_input()

    left_socks = socks[:l]
    right_socks = socks[l:]
    
    l_count = Counter(left_socks)
    r_count = Counter(right_socks)
    
    for color in l_count:
        if color in r_count:
            matched = min(l_count[color], r_count[color])
            l_count[color] -= matched
            r_count[color] -= matched
            l -= matched
            r -= matched

    if l < r:
        l, r = r, l
        l_count, r_count = r_count, l_count

    ans = 0
    diff = (l - r) // 2
    
    for color in l_count:
        temp = l_count[color] // 2
        mins = min(diff, temp)
        ans += mins
        diff -= mins
        l -= 2 * mins 

    ans += diff  
    ans += (l + r) // 2 
    
    print(ans)