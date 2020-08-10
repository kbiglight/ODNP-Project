# Tag : Stack, Recursion
# no additional input files
import sys

input: () = lambda: sys.stdin.readline().strip()


def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N - 1)


N = int(input())
fact = factorial(N)
# print(fact)
stack = list(str(fact))
# print(stack)
count = 0

while stack.pop() == '0':
    count += 1

print(count)
