# 토마토 / Silver I

import sys
# from util import DatetimeDecorator
from collections import deque
from pprint import pprint as pp

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_7576', 'r')

m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
days = [[-1 for _ in range(m)] for _ in range(n)]

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


# @DatetimeDecorator
def solution():
    queue = deque()

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                days[j][i] = 0
                queue.append((i, j))

    while queue:
        x, y = map(int, queue.popleft())
        if days[y][x] >= 0:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0 and days[ny][nx] == -1:
                    days[ny][nx] = days[y][x] + 1
                    queue.append((nx, ny))

    for i in range(m):
        for j in range(n):
            if days[j][i] == -1 and graph[j][i] == 0:
                return -1

    return max(max(days))


result = solution()
print(result)
