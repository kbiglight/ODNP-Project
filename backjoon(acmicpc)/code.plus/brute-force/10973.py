import sys
import copy
input = sys.stdin.readline


def prev_permutation(lst):
    i = len(lst) - 1  # 리스트의 마지막 인덱스
    while i > 0 and lst[i - 1] <= lst[i]:
        i -= 1

    if i == 0:
        return False

    lst[i - 1], lst[i] = lst[i], lst[i - 1]
    print("i =", i)
    j = len(lst) - 1

    # while i < j
    return True


def prev_permutation2(a):
    n = len(a) - 1
    i = n
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i == 0:
        return False
    j = n
    while a[i - 1] <= a[j]:
        j -= 1

    print("n = {}, i = {}, j = {}".format(n, i, j))
    a[i - 1], a[j] = a[j], a[i - 1]
    # j = n
    # while i < j:
    #     a[i], a[j] = a[j], a[i]
    #     i += 1
    #     j -= 1
    return True


N = int(input())
target = list(map(int, input().split()))
target2 = copy.deepcopy(target)
if prev_permutation(target):
    print(target)

if prev_permutation2(target2):
    print(target2)
