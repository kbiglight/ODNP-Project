# 숫자카드 2 / Silver IV

import sys
from collections import Counter
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_10816', 'r')


@DatetimeDecorator
def solution(n, n_card_list, m, m_card_list):
    answer = []

    n_card_list.sort()
    for card in m_card_list:
        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2

            if n_card_list[mid] == card:
                while n_card_list[mid] == card:
                    pass

            elif n_card_list[mid] < card:
                start = mid + 1
            else:
                end = mid - 1

        # answer.append(counter[card])

    print(n_card_list)
    return ' '.join(map(str, answer))


n = int(input())
n_card_list = list(map(int, input().split()))

m = int(input())
m_card_list = list(map(int, input().split()))

result = solution(n, n_card_list, m, m_card_list)
print(result)
