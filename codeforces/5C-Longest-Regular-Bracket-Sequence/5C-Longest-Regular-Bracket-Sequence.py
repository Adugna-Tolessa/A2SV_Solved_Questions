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

s = string_input()
stack = [-1]
longest = 0
cnt = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        stack.pop()
        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            if length > longest:
                longest = length
                cnt = 1
            elif length == longest:
                cnt += 1

if longest == 0:
    print(0, 1)
else:
    print(longest, cnt)