# Title / Difficulty
# 8진수, 10진수, 16진수 / Bronze Ⅰ

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('inputs/input_boj_11816', 'r')


@DatetimeDecorator
def solution(n):
    if n[0] == '0':
        if n[1] == 'x':
            return int(n, 16)
        else:
            return int(n, 8)

    else:
        return int(n)


n = input()
print(solution(n))
