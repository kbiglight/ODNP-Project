# 숫자카드 / 

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_10815', 'r')

@DatetimeDecorator
def solution(n, card_list, m, chk_card_list):
    answer = [0 for _ in range(m)]
    # chk_list = [False for _ in range(-10000000, 10000001)]
    chk_list = [False for _ in range(min(card_list), max(card_list)+1)]
    print(chk_list)
    for card in card_list:
        chk_list[card] = True

    print(chk_list)

    for i in range(m):
        if chk_list[chk_card_list[i]]:
            answer[i] = 1

    return ' '.join(map(str,answer))


n = int(input())
card_list = list(map(int, input().split()))

m = int(input())
chk_card_list = list(map(int, input().split()))

result = solution(n, card_list, m, chk_card_list)
print(result)
