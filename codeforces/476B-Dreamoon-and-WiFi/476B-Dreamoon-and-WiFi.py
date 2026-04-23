from collections import deque, Counter, defaultdict
import sys
import math
import bisect
import heapq
import itertools
# sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def int_input():
    return int(input().strip())
def map_input():
    return map(int, input().strip().split())
def list_input():
    return list(map(int, input().strip().split()))
def string_input():
    return input().strip()
def list_of_strings():
    return input().strip().split()


s1 = string_input()
s2 = string_input()

target = s1.count('+') - s1.count('-')

curr = 0
cnt = 0
for c in s2:
    if c == '+':
        curr += 1
    elif c == '-':
        curr -= 1
    else:
        cnt += 1

sol = 0
def backtrack(idx, tot):
    global sol
    if idx == cnt:
        if tot == target:
            sol += 1
        return
    backtrack(idx + 1, tot + 1)
    backtrack(idx + 1, tot - 1)

backtrack(0, curr)

total = 2 ** cnt
print(sol / total)