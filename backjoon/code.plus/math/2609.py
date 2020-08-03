# Title : 최대공약수와 최소공배수
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
# 입력
#   첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.
# 출력
#   첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# Commentary
# 최대공약수는 단순하게 사람이 두 수를 소인수 분해하여 겹치는 수를 찾아 구하는 그런 방법으로 접근하면 안된다.
# 여기서 사용해야 할 알고리즘은 유클리드 호제법(Euclidean Algorithm).
# "호제법"이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 의미한다
# 쉽게 말해 2개의 자연수 A, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, A>B), "a와 b의 최대공약수는 b와 r의 최대공약수와 같다"
#

import sys

input = lambda: sys.stdin.readline().strip()
sys.stdin = open('../../inputs/input_2609', 'r')

def gcd_recursive(A, B):
    if B > A:
        (A, B) = (B, A)

    # print(A, B)

    if (A % B) == 0:
        # print(B)
        return B
    else:
        return gcd_recursive(A % B, B)


# def gcd_iteration(A, B):
#     while B != 0:
#         (A, B) = (A % B, B)
#         if A < B:
#             (A, B) = (B, A)
#
#     return A


def lcd(A, B):
    GCD = gcd_recursive(A, B)

    return int(A * B / GCD)


A, B = map(int, input().split())

print(gcd_recursive(A, B))
# print(gcd_iteration(A, B))
print(lcd(A, B))
