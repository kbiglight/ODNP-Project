import sys
import timeit
# import logging_time

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_11653', 'r')

N = int(input())
start = timeit.default_timer()
chk_prime = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N + 1):
    if chk_prime[i]:
        primes.append(i)
        for j in range(i * 2, N + 1, i):
            chk_prime[j] = False

N1 = N
for prime in primes:
    # print(prime)
    while N1 % prime == 0:
        print(prime)
        N1 //= prime
    if N1 == 1:
        break
end = timeit.default_timer()
print(end - start)


N2 = N
start = timeit.default_timer()
while N2 != 1:
    for i in range(2, N2 + 1):
        # 나눠지면 출력하고,
        # 다음을 위해 해당 수로 num을 나눠줍니다.
        if N2 % i == 0:
            print(i)
            N2 //= i
            break
end = timeit.default_timer()
print(end - start)



