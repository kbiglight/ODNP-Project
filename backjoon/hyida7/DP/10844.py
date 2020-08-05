import sys
from util import DatetimeDecorator
from pprint import pprint as pp

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_10844', 'r')


@DatetimeDecorator
def get_start_num_list(n):
    cache = [0 for _ in range(n)]

    count = 0
    prob_count = 0
    for i in range(0, 10):
        if i == 0:
            continue
        for j in range(0, 10):
            if j == i + 1 or j == i - 1:
                for k in range(0, 10):
                    if k == j + 1 or k == j - 1:
                        print(i * 100 + j * 10 + k)
                        count += 1
                        if k == 0 or k == 9:
                            # print(i * 10000 + j * 1000 + k * 100 + l * 10 + h)
                            prob_count += 1
                        # for l in range(0, 10):
                        #     if l == k + 1 or l == k - 1:
                        #         for h in range(0, 10):
                        #             if h == l + 1 or h == l - 1:
                        #                 print(i * 10000 + j * 1000 + k * 100 + l * 10 + h)
                        #                 count += 1
                        #                 if h == 0 or h == 9:
                        #                     print(i * 10000 + j * 1000 + k * 100 + l * 10 + h)
                        #                     prob_count += 1

    print(count, prob_count)
    return count


n = int(input())
count = get_start_num_list(n)


# result = get_stair_num_count(n)
# get_stair_num_count2(2)
# # print(count)
# print(result % 1000000000)

def stair_num_count(n):
    cache = [[0 for _ in range(10)] for _ in range(n + 1)]

    for i in range(10):
        if i == 0:
            continue

        cache[1][i] = 1

    for j in range(2, n + 1):
        for k in range(10):
            if k == 0:
                cache[j][k] = cache[j - 1][k + 1]

            elif k == 9:
                cache[j][k] = cache[j - 1][k - 1]

            else:
                cache[j][k] = cache[j - 1][k + 1] + cache[j - 1][k - 1]

    pp(sum(cache[n]))

    pp(cache)

    return sum(cache[n])


n = int(input())
result = stair_num_count(n)
print(result % 1000000000)

# n1 = int(input())
