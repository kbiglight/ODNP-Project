import sys

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../Codes/backjoon/inputs/input_11576')

A, B = map(int, input().split())
m = int(input())
num_list = list(map(int, input().split()))

decimal = 0
i = 1
while num_list:
    num = num_list.pop()
    decimal += num * i
    i *= A

B_list = []
while decimal > 0:
    B_list.append(decimal % B)
    decimal //= B

print(' '.join(map(str, reversed(B_list))))
