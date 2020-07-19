# input에 관련하여...

현재 내가 가장 많이 쓰는 input 방식은 다음과 같다
```python
import sys

input = sys.stdin.readline
# or
# input = lambda: sys.stdin.readline().strip()

# 한개 입력
N = input()

# 여러 개 입력
A, B = input().split()
# or
X, Y = map(int, input().split())

# 입력 리스트화 하기
my_list = list(input())
```

이렇게 되면 한 줄을 전체로 입력을 받는다.  
여기서 중요한 것은 입력에서 한 줄의 기준이 되는 '\n'인 Enter까지 받아온다


---
하지만 이렇게 sys 모듈을 불러와서 