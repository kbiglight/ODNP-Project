# ABCDE / Gold V

import sys
from util import DatetimeDecorator
from collections import deque
from pprint import pprint as pp

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_13023', 'r')


# 재귀함수를 이용한 풀이
def solution(v, count):
    # print('count = {}'.format(count))
    global answer
    if count == 4:
        answer = True
        return 1

    visited[v] = True

    for target in graph[v]:
        if not visited[target]:
            # print('v : {}, graph[{}] : {} target : {} {} count : {}'.format(v, v, graph[v], target, visited, count))
            solution(target, count + 1)
            visited[target] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n)]
answer = False
for i in range(n):
    result = solution(i, 0)
    visited[i] = False

    if answer:
        break

print(1 if answer else 0)
