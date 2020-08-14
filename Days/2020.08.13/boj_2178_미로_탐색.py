# 미로 탐색 / Silver I

import sys
from util import DatetimeDecorator
from collections import deque
from pprint import pprint as pp

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_2178', 'r')


# search shortest path in maze.
# which means, use bfs
def solution():
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    graph_path = [[-1 for _ in range(m)] for _ in range(n)]
    graph_path[0][0] = 1
    queue = deque([(0, 0, 1)])

    while queue:
        print(queue)
        pp(graph_path)
        p_x, p_y, count = map(int, queue.popleft())
        for i in range(4):
            n_x, n_y = p_x + dx[i], p_y + dy[i]
            if 0 <= n_x < m and 0 <= n_y < n and graph[n_y][n_x] == '1' and graph_path[n_y][n_x] == -1:
                graph_path[n_y][n_x] = count + 1
                queue.append((n_x, n_y, count + 1))

    # pp(graph_path)
    return graph_path[n - 1][m - 1]


n, m = map(int, input().split())
graph = []
for _ in range(n):
    line = list(input())
    graph.append(line)

# pp(graph)

result = solution()
print(result)
