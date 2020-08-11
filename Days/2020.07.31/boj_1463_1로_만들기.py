import sys
from util import DatetimeDecorator

sys.setrecursionlimit(5000)

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../Codes/backjoon/inputs/input_1463')


# @DatetimeDecorator
# first try
# def fill_cache(N, cache):
#     # print(cache)
#     if N == 1:
#         return
#
#     # print(cache[N - 1], cache[N])
#     if cache[N - 1] > cache[N]:
#         cache[N - 1] = cache[N] + 1
#         # print('{} {} {}'.format(N, N - 1, cache[N - 1]))
#         fill_cache(N - 1, cache)
#
#     # print(cache[N - 1], cache[N])
#     if N % 2 == 0 and cache[N // 2] > cache[N]:
#         cache[N // 2] = cache[N] + 1
#         # print('{} {} {}'.format(N, N // 2, cache[N // 2]))
#         fill_cache(N // 2, cache)
#         # print(N)
#
#     if N % 3 == 0 and cache[N // 3] > cache[N]:
#         cache[N // 3] = cache[N] + 1
#         # print('{} {} {}'.format(N, N // 3, cache[N // 3]))
#         fill_cache(N // 3, cache)

@DatetimeDecorator
def fill_cache(N, cache):
    if N == 1:
        return

    for i in range(N, 0, -1):
        if i % 3 == 0 and cache[i // 3] > cache[i] + 1:
            cache[i // 3] = cache[i] + 1

        if i % 2 == 0 and cache[i // 2] > cache[i] + 1:
            cache[i // 2] = cache[i] + 1

        if cache[i - 1] > cache[i] + 1:
            cache[i - 1] = cache[i] + 1

    # print(N)
    # print(cache[N - 1])

    # for i in range(N, 0, -1):
    #     if i % 3 == 0 and cache[i // 3] + 1 > cache[N]:
    #         cache[i // 3] = cache[i] + 1
    #         print('{} {} {}'.format(i, i // 3, cache[i // 3]))
    #         # fill_cache(i // 3, cache)
    #
    #         # print(i)
    #     print(cache[i - 1], cache[i])
    #     if i % 2 == 0 and cache[i // 2] + 1 > cache[N]:
    #         cache[i // 2] = cache[i] + 1
    #         print('{} {} {}'.format(i, i // 2, cache[i // 2]))
    #         # fill_cache(i // 2, cache)
    #
    #     if cache[i - 1] + 1 > cache[N]:
    #         cache[i - 1] = cache[i] + 1
    #         print('{} {} {}'.format(i, i - 1, cache[i - 1]))
    #         # fill_cache(i - 1, cache)
    #
    #     print(cache)


N = int(input())
cache = [N for _ in range(N)] + [0]
fill_cache(N, cache)
print(cache[1])
