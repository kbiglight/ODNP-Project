import sys
from string import ascii_uppercase, digits

input: () = lambda: sys.stdin.readline().strip()
# file input
# sys.stdin = open('../../inputs/input_11005', 'r')

LETTERS = list(digits) + list(ascii_uppercase)


# print(LETTERS)

def change_numeric_system(target, n):
    answer = []

    print(target // 36, target / 36)

    while target > 0:
        result = target % n
        answer.append(LETTERS[result])
        target //= n

    # print(degree)
    # print(target)
    return reversed(answer)


target, n = map(int, input().split())
result = change_numeric_system(target, n)
print(''.join(result))
