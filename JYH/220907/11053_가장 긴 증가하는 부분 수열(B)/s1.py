# 11053_가장 긴 증가하는 부분 수열(B)
# 2022_09_05

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A = list(map(int, input().split()))

dp = [1]*N
for i in range(N):
    for j in range(i):
        midV = 0
        if A[i] > A[j]:
            midV = dp[j] + 1
        if midV > dp[i]:
            dp[i] = midV

print(max(dp))