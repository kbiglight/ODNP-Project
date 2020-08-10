# 숫자카드 2 / Silver IV

import sys
import math
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_10816', 'r')


@DatetimeDecorator
def solution(n, n_card_list, m, m_card_list):
    answer = []
    count_list = [0 for _ in range(min(n_card_list), max(n_card_list) + 1)]

    for card in n_card_list:
        count_list[card + abs(min(n_card_list))] += 1

    for card in m_card_list:
        answer.append(count_list[card + abs(min(n_card_list))])

    return ' '.join(map(str, answer))


n = int(input())
n_card_list = list(map(int, input().split()))

m = int(input())
m_card_list = list(map(int, input().split()))

result = solution(n, n_card_list, m, m_card_list)
print(result)
