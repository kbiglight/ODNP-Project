# DFS와 BFS / Silver II

import sys
from util import DatetimeDecorator
from collections import deque

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('inputs/input_boj_1260', 'r')


# dfs
def dfs(v, graph=None):
    print(graph)
    queue = deque([v])
    visited = []

    while queue:
        print(queue)
        target = queue.popleft()
        if target not in visited:
            visited.append(target)
            queue = deque(graph[target]) + queue

    print(' '.join(map(str, visited)))


# bfs
def bfs(v, graph):
    stack = deque([v])
    visited = []

    while stack:
        # print(stack)
        target = stack.popleft()
        if target not in visited:
            visited.append(target)
            stack.extend((graph[target]))

    print(' '.join(map(str, visited)))


# print(input())
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]  # n명 만큼의 비어있는 list의 graph 생성
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


# 왜 이문제에서 요소들을 정렬해줄 필요가 있을까?
for element in graph:
    element.sort()

dfs(v, graph)
bfs(v, graph)

# dfs(v)
# bfs(v)
