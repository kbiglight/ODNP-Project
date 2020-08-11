import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_11052')


@DatetimeDecorator
def get_max_price(n, p_list):  # make cache and get highest value
    cache = [0 for _ in range(n + 1)]
    # cache[1] = p_list[1]

    # Bottom-UP
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            # print("i = {} | j = {} | cache[{}] = {} | cache[{}] + p_list[{}] = {}"
            #       .format(i, j, i, cache[i], i-j, j, cache[i - j] + p_list[j]))
            cache[i] = max(cache[i], cache[i - j] + p_list[j])

    # print(cache)
    return cache[n]


n = int(input())
p_list = [0] + list(map(int, input().split()))
result = get_max_price(n, p_list)
print(result)
