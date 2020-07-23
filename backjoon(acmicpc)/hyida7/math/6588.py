# Title : 골드바흐의 추측
# Link  : https://www.acmicpc.net/problem/6588
# tag   : 에라토스테네스의 체, 정수론
#
# 문제
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.
# [ 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다. ]
# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다.
# 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.
#
# 이 추측은 아직도 해결되지 않은 문제이다.
#
# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
#
# Input
# 입력은 하나 또는 그 이상의 테스트 케이스로 이루어져 있다. 테스트 케이스의 개수는 100,000개를 넘지 않는다.
# 각 테스트 케이스는 짝수 정수 n 하나로 이루어져 있다. (6 ≤ n ≤ 1000000)
# 입력의 마지막 줄에는 0이 하나 주어진다.
#
# Output
# 각 테스트 케이스에 대해서, n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다. 숫자와 연산자는 공백 하나로 구분되어져 있다.
# 만약, n을 만들 수 있는 방법이 여러 가지라면, b-a가 가장 큰 것을 출력한다.
# 또, 두 홀수 소수의 합으로 n을 나타낼 수 없는 경우에는 "Goldbach's conjecture is wrong."을 출력한다.


# Solution

import sys

input = lambda: sys.stdin.readline().strip()
# sys.stdin = open("../../inputs/input_6588.txt", 'r')

# 0. 준비물 : 소수들의 집합(list)
# 에라토스테네스의 체를 통해 미리 소수들의 집합을 구해놓음
# MAX_NUM = 1000000
# chk_prime = [False, False] + [True] * (MAX_NUM - 1)
# primes = []
# for i in range(2, MAX_NUM + 1):
#     if chk_prime[i]:
#         primes.append(i)
#         for j in range(i * 2, MAX_NUM + 1, i):
#             chk_prime[j] = False
# print(prime)
# while 1:
#     N = int(input())
#     if N == 0:
#         break
#
#     for i in range(len(prime)):
#         if prime[i] > N:
#             print("Goldbach's conjecture is wrong.")
#             break
#
#         if (N - prime[i]) in prime:
#             print("{} = {} + {}".format(N, prime[i], N - prime[i]))
#             break
#
#    ----------------------------
#   |       시간 초과 엔딩         |
#    ----------------------------
#
# 이유 예측
# 1. 먼저 에레토스테네스의 체를 이용해서 소수들을 구할 때 반복문 조건을
#    i*2로 안주고 i로 줘서 불필요한 연산을 했어야 함
# 2. primes 리스트에는 소수들의 집합이 들어가있지만
#    chk_prime은 소수인지를 판별하는 리스트이다. 즉 primes 리스트에
#    값이 있는지를 확인하는 것이 아닌 chk_prime 리스트에 해당 인덱스의
#    참 거짓을 보면 이 값이 소수인지를 판별할 수 있다. 그만큼 리스트 전체를 확인해야 하는
#    불필요한 연산이 추가가 되었다. 다시말해 가지고있는 정보를 백분 활용하지 못했다.


# 다시 풀이. 즉 오답노트의 답
MAX_NUM = 1000000
chk_prime = [False, False] + [True] * (MAX_NUM - 1)
primes = []
for i in range(2, MAX_NUM + 1):
    if chk_prime[i]:
        primes.append(i)
        for j in range(i * 2, MAX_NUM + 1, i):
            chk_prime[j] = False

while 1:
    N = int(input())
    if N == 0:
        break

    for prime in primes:
        if prime > N:
            print("Goldbach's conjecture is wrong.")
            break

        if chk_prime[N - prime]:
            print("{} = {} + {}".format(N, prime, N - prime))
            break
