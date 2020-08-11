# 별 찍기 17 / Bronze III

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()


def solution(n):
    pivot = n - 1

    print(' ' * pivot + '*')
    for i in range(1, n - 1):
        pivot -= 1
        print(' ' * pivot + '*' + ' ' * ((2 * i) - 1) + '*')

    if n > 1:
        print("*" * ((2 * n) - 1))


n = int(input())
solution(n)
