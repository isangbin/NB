# BOJ_1182 부분수열의 합 문제풀이
# 2022-09-26

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

cnt = 0
for i in range(1, 1 << N):
    cur_sum = 0
    for j in range(N):
        if i & (1 << j):
            cur_sum += numbers[j]

    if cur_sum == S:
        cnt += 1

print(cnt)