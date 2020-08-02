import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_11727')


@DatetimeDecorator
def make_cache(n):
    cache = [0 for _ in range(n + 1)]
    if n >= 1:
        cache[1] = 1

    if n >= 2:
        cache[2] = 3

    if n >= 3:
        for i in range(3, n + 1):
            cache[i] = cache[i - 1] + 2 * cache[i - 2]

    return cache


n = int(input())
cache = make_cache(n)
print(type(cache))
print(cache[n] % 10007)
