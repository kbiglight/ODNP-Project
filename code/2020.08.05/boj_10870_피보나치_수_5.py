# Title / Difficulty
# 피보나치 수 5 / Bronze Ⅱ

# 눈치챘겠지만 2747번과 같은 풀이다. 토시하나 틀리지 않고

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()


@DatetimeDecorator
def solution(n):
    cache = [0, 1, 1] + [0 for _ in range(n - 2)]

    for i in range(3, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


n = int(input())
result = solution(n)
print(result)
