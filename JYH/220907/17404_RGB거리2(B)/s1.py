# 17404_RGB거리2(B)
# 2022-09-04

import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cost = []
for _ in range(N):
    R, G, B = map(int, input().split())
    cost.append((R, G, B)) # [(26, 40, 83), (49, 60, 57), (13, 89, 99)]

initial = 1000
answer = 1000*1000
dp = [[0]*3 for _ in range(N)] # N행 3열
for i in range(3): # 시작점 3개로 첫 번째 집을 R로 칠할 때, G로 칠할 때, B로 칠할 때 나눠서 생각
    dp[0] = [initial, initial, initial]
    dp[0][i] = cost[0][i]
    for j in range(1, N): # j번째 집을
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2]) # R로 칠한다면, (cost에서 R값)과 (전 집이 G로 칠한경우와 B로 칠한경우 중 작은 값)을 더한다. 
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2]) # G로 칠한다면,
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1]) # B로 칠한다면,

    # j가 N-1이 되었을 때, 가장 작은 값을 answer에 저장 => 시작점(i)을 바꿔서 또 비교
    answer = min(answer, dp[j][(i+1)%3], dp[j][(i+2)%3]) # 가장 마지막 집은 가장 첫 집이랑 색이 달라야 하기 때문에 %3을 이용한다. 

print(answer)
