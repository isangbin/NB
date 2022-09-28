import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

if S == 0:
    cnt = -1                        # S=0이면 공집합이 체크될 우려
else:
    cnt = 0

for i in range(1 << N):
    summary = 0
    for j in range(N):
        if i & (1 << j):
            summary += nums[j]

    if summary == S:
        cnt += 1

print(cnt)