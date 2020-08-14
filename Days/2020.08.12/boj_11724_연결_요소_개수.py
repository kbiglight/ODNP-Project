# 연결 요소 개수 / Silver II

import sys
from util import DatetimeDecorator
from collections import deque

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_11724', 'r')

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(n + 1)]


def solution(v):
    visited[v] = True

    queue = deque(graph[v])

    while queue:
        target = queue.popleft()
        if not visited[target]:
            visited[target] = True
            queue.extendleft((reversed(graph[target])))


count = 0
for i in range(1, n+1):
    print(i)
    if not visited[i]:
        solution(i)
        count += 1

print(count)
