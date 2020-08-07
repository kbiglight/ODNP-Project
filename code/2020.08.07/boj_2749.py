# Title / Difficulty
# 피보나치 수 3 / Gold Ⅲ

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('inputs/input_boj_2749', 'r')


@DatetimeDecorator
def solution(n):
    cache = [0, 1, 1]

    for i in range(3, n + 1):
        cache[i % 3] = (cache[(i - 1) % 3] + cache[(i - 2) % 3])
    print(cache[n % 3])
    print(cache[n % 3] % 1000000)


n = input()
print(n)
print(int(n))
print(2 ** 32)

solution(int(n))
# print(solution(n))
