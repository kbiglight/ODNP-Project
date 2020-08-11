import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_9095')


def get_case_number(N):
    cache = [0 for _ in range(0, N + 1)]

    if N >= 1:
        cache[1] = 1

    if N >= 2:
        cache[2] = 2

    if N >= 3:
        cache[3] = 4

    if N >= 4:
        for i in range(4, N + 1):
            cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3]

    # print(cache)
    return cache[N]


T = int(input())

for _ in range(T):
    N = int(input())
    print(get_case_number(N))
