# 1182_부분수열의 합(B)
# 2022-09-22

import sys
sys.stdin = open('input.txt', 'r')

N, S = map(int, input().split())
N_number = list(map(int, input().split()))

cnt = 0
for i in range(1, 1<<N):
    sums = 0
    for j in range(N):
        if i & (1<<j):
            sums += N_number[j]
    if sums == S:
        cnt += 1

print(cnt)