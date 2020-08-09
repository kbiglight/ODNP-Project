# 중복 빼고 정렬하기 / Silver V

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_10867', 'r')


@DatetimeDecorator
def solution(n, num_list):
    new_num_list = []
    chk_num = [False for _ in range(-1000, 1001)]

    for num in num_list:
        if not chk_num[num]:
            chk_num[num] = True
            new_num_list.append(num)

    new_num_list.sort()
    return ' '.join(map(str, new_num_list))


n = int(input())
num_list = list(map(int, input().split()))
result = solution(n, num_list)
print(result)
