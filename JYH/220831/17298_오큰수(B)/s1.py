# 17298_오큰수(B)
# 2022-08-28

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))

stack = []
result = []
while A != []:
    # stack에 넣고 A에서 빼내기
    stack.append(A[0])
    A.pop(0)
    # stack 마지막 값과 남아있는 A 원소들 비교
    for value in A:
        if stack[-1] < value:
            result.append(value)
            break
    else:
        result.append(-1)
    
print(*result)
# 시간 초과..