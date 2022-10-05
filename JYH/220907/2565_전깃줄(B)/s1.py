# 2565_전깃줄(B)
# 2022-09-03

import sys
sys.stdin = open('input.txt', 'r')

N = int(input()) # 전깃줄 개수
L = []
for _ in range(N):
    A, B = map(int, input().split())
    L.append((A, B))

L.sort() # [(1, 8), (2, 2), (3, 9), (4, 1), (6, 4), (7, 6), (9, 7), (10, 10)]

new_L = []
for i in range(N):
    new_L.append(L[i][1]) # [8, 2, 9, 1, 4, 6, 7, 10]

# 가장 긴 증가하는 부분수열 구하기(LIS)
dp = [1]*N # [1, 1, 1, 1, 1, 1, 1, 1]
for i in range(N):
    for j in range(i): # 현재 자기 위치 i보다 앞쪽의 값들을 비교
        if new_L[i] > new_L[j]: # 만약 자기 위치 i보다 앞의 값 j가 크다면 
            dp[i] = max(dp[i], dp[j]+1) # 자기 위치에 있는 dp값과 j의 dp값 + 1 중 더 큰 값을 채택
 
print(N - max(dp))