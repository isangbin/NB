# BOJ_2565 전깃줄
# 2022-09-05

N = int(input())


lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()
lines_b = []

dp = [0 for i in range(N)]

for i in range(N):
    lines_b.append(lines[i][1])

for i in range(N):
    for j in range(N):
        if lines_b[i] > lines_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(N - max(dp))