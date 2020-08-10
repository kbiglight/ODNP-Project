import sys
from string import ascii_uppercase, digits

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../backjoon/inputs/input_2745', 'r')
# LETTERS = list(digits) + list(ascii_uppercase)
# LETTERS = [(v, i) for i, v in enumerate(digits+ascii_uppercase)]
# Letters = dict(LETTERS)
# print(LETTERS)
LETTERS = dict([(v, i) for i, v in enumerate(digits + ascii_uppercase)])


def to_decimal(N, B):
    result = 0
    i = 1
    while N:
        num = N.pop()
        result += LETTERS[num] * i
        # print("{} {} {}".format(num, i, result) )
        i *= B

    return result


N, B = map(str, input().split())
N = list(N)
B = int(B)
result = to_decimal(N, B)
print(result)
