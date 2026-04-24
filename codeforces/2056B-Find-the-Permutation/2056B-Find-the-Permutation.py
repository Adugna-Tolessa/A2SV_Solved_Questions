from collections import deque, Counter, defaultdict
import sys
from math import gcd
from bisect import bisect_left, bisect_right
from heapq import heapify, heappop, heappush
import itertools
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

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

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(string_input())
    # temp = [0] * n
    # for i in range(n):
    #     for j in range(n):
    #         temp[i] += int(matrix[j][i])
    # idx = list(range(n))
    # idx.sort(key=lambda i: (temp[i], -i))
    # for i in range(n):
    #     idx[i] += 1
    # print(*idx)
               
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == '1':
                graph[i].append(j)
            else:
                graph[j].append(i)
    # print(graph)
    visited = [False] * n
    order = []

    def dfs(node):
        visited[node] = True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)
        order.append(node)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    order.reverse()

    print(*[m + 1 for m in order])