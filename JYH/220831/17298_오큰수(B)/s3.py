# 17298_오큰수(B)
# 2022-08-28

import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
A = list(map(int, input().split()))

stack = deque() # deque 쓰면 시간 단축 효과
result = [-1]*N # 기본 -1로 설정 (마지막 수를 -1로 하기 위해)
for i in range(N):
    while stack: # 이전에 저장되어 있던 stack의 원소들도 비교, A[i]가 7이 들어올 때 stack에 남아있는 A[2] 비교 후 A[1]도 비교
        if A[i] > A[stack[-1]]:
            result[stack.pop()] = A[i] # 인덱스를 pop해서 result 리스트에서 사용
        else: # 작은 값 들어오면 아무 일 하지 않고 stack에 쌓기
            break
    stack.append(i) # 인덱스를 저장
    
print(*result)
# 구글링 해서 공부함..