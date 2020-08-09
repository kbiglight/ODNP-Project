import sys
from util import DatetimeDecorator
from pprint import pprint as pp

input: () = lambda: sys.stdin.readline().strip()


@DatetimeDecorator
def stair_num_count(n):
    cache = [[0 for _ in range(10)] for _ in range(n + 1)]

    for i in range(10):
        if i == 0:
            continue

        cache[1][i] = 1

    for j in range(2, n + 1):
        for k in range(10):
            if k == 0:
                cache[j][k] = cache[j - 1][k + 1]

            elif k == 9:
                cache[j][k] = cache[j - 1][k - 1]

            else:
                cache[j][k] = cache[j - 1][k + 1] + cache[j - 1][k - 1]

    # pp(sum(cache[n]))
    # pp(cache)
    return sum(cache[n])


n = int(input())
result = stair_num_count(n)
print(result % 1000000000)
