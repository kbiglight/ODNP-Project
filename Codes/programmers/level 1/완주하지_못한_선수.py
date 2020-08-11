# hash
def solution(participant, completion):
    answer = ''
    stack = participant + completion

    stack = sorted(stack)
    chk_list = [False for _ in range(len(stack))]

    for i in range(len(stack) - 1, 0, -1):
        if stack[i] == stack[i - 1] and chk_list[i] == chk_list[i - 1]:
            chk_list[i] = chk_list[i - 1] = True

    for i in range(len(chk_list)):
        if not chk_list[i]:
            answer = stack[i]
    return answer
