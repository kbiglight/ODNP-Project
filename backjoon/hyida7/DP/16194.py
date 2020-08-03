import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_16194', 'r')


@DatetimeDecorator
def get_min_price(n, p_list):
    cache = [0] + [max(p_list) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # print("i = {} | j = {} | cache[{}] = {} | cache[{}] + p_list[{}] = {}"
            #       .format(i, j, i, cache[i], i-j, j, cache[i - j] + p_list[j]))
            cache[i] = min(cache[i], cache[i - j] + p_list[j])
            print(cache)


    return cache[n]

n = int(input())
p_list = [0] + list(map(int, input().split()))
# print(p_list)
result = get_min_price(n, p_list)
print(result)
