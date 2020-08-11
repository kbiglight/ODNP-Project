import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_15990', 'r')


@DatetimeDecorator
def get_(n):
    cache = [0 for _ in range(n + 1)]

    if n >= 1:
        cache[1] = 1

    if n >= 2:
        cache[2] = 2

    if n >= 3:
        cache[3] = 4

    if n>=4:
        for i in range(4, n+1):
            cache[i] = cache[i-1]


    return cache[n]


t = int(input())
for _ in range(t):
    n = int(input())

