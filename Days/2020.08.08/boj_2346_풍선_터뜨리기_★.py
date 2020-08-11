# 풍선 터뜨리기 / Silver III

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_2346', 'r')


@DatetimeDecorator
def solution(n, balloons):
    pop_seq = [1]
    target = 0

    for i in range(1, n+1):
        balloon = balloons[target]
        balloons.pop(target)
        if balloon > 0:
            temp = balloon % n
            target = (target - 1 + (balloon % n)) % n
        elif balloon < 0:
            temp = balloon % n
            target = (target - 1 + (balloon % n)) % n

        pop_seq.append(target + 1 + i)
        n -= 1
        # target -= 1 # length change(pop)
        print(target, balloons)

    return pop_seq


n = int(input())
balloons = list(map(int, input().split()))
print(enumerate(balloons))
result = solution(n, balloons)
print(result)
