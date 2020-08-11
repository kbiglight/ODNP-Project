import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../Codes/backjoon/inputs/input_11726')


@DatetimeDecorator
def make_cache(n):
    cache = [0 for _ in range(n + 1)]
    if n >= 1:
        cache[1] = 1
    if n >= 2:
        cache[2] = 2

    if n >= 3:
        for i in range(3, n + 1):
            cache[i] = cache[i - 2] + cache[i - 1]

    return cache


n = int(input())
cache = make_cache(n)
# print(cache)
# print(len(cache))
print(cache[n] % 10007)
