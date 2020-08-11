import sys

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_17413')

line = input()
bracket = False
result = list()
word = list()

for letter in line:
    if bracket:
        if letter == '>':
            bracket = False
            word.append(letter)
            result.append(''.join(word))
            word.clear()
        else:
            word.append(letter)
    elif not bracket:
        if letter == '<':
            if word:
                word.reverse()
                result.append(''.join(word))
                word.clear()
            bracket = True
            word.append(letter)
        elif letter == ' ':
            word.reverse()
            word.append(letter)
            result.append(''.join(word))
            word.clear()
        else:
            word.append(letter)

if word:
    word.reverse()
    result.append(''.join(word))

print(''.join(result))
