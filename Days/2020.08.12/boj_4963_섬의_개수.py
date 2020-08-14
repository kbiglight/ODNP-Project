# 섬의 개수 / Silver II

import sys
# from util import DatetimeDecorator
from pprint import pprint as pp


input: () = lambda: sys.stdin.readline().strip()
# file input
# sys.stdin = open('./inputs/input_boj_4963', 'r')
sys.setrecursionlimit(10**6)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def dfs(y, x, count):
    visited[y][x] = count
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1 and visited[ny][nx] == 0:
            dfs(ny, nx, count)


# 이거 bfs로도 풀수 있나?
# def bfs()???

def solution():
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                count += 1
                dfs(i, j, count)

    return count


while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))
    pp(graph)
    visited = [[0 for _ in range(w)] for _ in range(h)]

    result = solution()
    pp(visited)
    print(result)
