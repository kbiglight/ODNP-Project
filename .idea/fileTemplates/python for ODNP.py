import sys
from util import DatetimeDecorator

input: () = lambda: sys.stdin.readline().strip()
# file input
sys.stdin = open('../../inputs/input_${NAME}', 'r')