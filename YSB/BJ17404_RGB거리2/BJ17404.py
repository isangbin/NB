
import sys

n = int(sys.stdin.readline())
rgb = []
big = 1001
ans = big
for _ in range(n):
    rgb.append(list(map(int, sys.stdin.readline().split())))
print(rgb, 'rgb')
for i in range(3):
    dp = [[big, big, big] for _ in range(n)]
    dp[0][i] = rgb[0][i] # 첫집 색깔 내가 정함
    print(dp, 'dp1')
    print()

    for j in range(1, n):   # 두번째집부터 색깔 비용의 누적
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])
        print(dp, 'dp2')
        print()

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)