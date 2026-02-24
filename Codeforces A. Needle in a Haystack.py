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

T = int_input()
for _ in range(T):
    s = list(string_input())
    t = list(string_input())
    s_cnt = Counter(s)
    t_cnt = Counter(t)
    diff = t_cnt - s_cnt
    temp = []

    for key in s_cnt:
        if s_cnt[key] > t_cnt[key]:
            print("Impossible")
            break
    else:
        for key in diff:
            temp.extend([key] * diff[key])
        temp.sort()

        l = 0
        r = 0
        ans = []

        while l < len(s) and r < len(temp):
            if temp[r] < s[l]:
                ans.append(temp[r])
                r += 1
            else:
                ans.append(s[l])
                l += 1

        if s[l:]:
            ans.extend(s[l:])
        elif temp[r:]:
            ans.extend(temp[r:])

        print("".join(ans))
