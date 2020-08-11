# 에디터 / Silver III

import sys
from util import DatetimeDecorator
from collections import deque

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_1406', 'r')


@DatetimeDecorator
def solution(word, n, command_list):
    left, right = deque(word), deque()
    print(left, right)
    for i in range(n):
        command = command_list[i].split()
        if command[0] == 'L':
            if left:
                right.appendleft(left.pop())

        elif command[0] == 'D':
            if right:
                left.append(right.popleft())

        elif command[0] == 'B':
            if left:
                left.pop()

        elif command[0] == 'P':
            left.append(command[1])

    return ''.join(left + right)


word = input()
n = int(input())
command_list = []
for _ in range(n):
    command_list.append(input())

result = solution(word, n, command_list)
print(result)
