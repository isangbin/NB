# 17298_오큰수(B)
# 2022-08-28

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
result = [-1] # 마지막 값은 항상 -1이므로

# 뒤부터 탐색
maxV = A[-1]
for i in range(N-1, 0, -1):
    if A[i] < A[i-1]: # 앞의 수가 더 크다면
        if A[i-1] > maxV: # 근데 앞의 수가 maxV보다 크다면
            maxV = A[i-1]
            result = [-1] + result
        else: # 앞의 수가 maxV보다 작다면
            result = [maxV] + result
    else: # 앞의 수가 더 작다면
        maxV = A[i]
        result = [maxV] + result

print(*result)
# 시간 초과..