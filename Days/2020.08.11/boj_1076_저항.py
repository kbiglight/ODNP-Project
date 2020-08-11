# 저항 / Bronze 2

import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('./inputs/input_boj_1076', 'r')

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
rev_color = [(v,k) for k,v in enumerate(color)]


resist = dict(rev_color)
print(resist)

first = input()
second = input()
third = input()

result = (resist[first] * 10 + resist[second]) * (10**resist[third])
print(result)
