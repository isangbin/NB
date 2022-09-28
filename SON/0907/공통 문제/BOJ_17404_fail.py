# BOJ_17404 RGB 거리 2
# 2022-09-04

N = int(input())
costs = []
min_result = [[0, 0, 0] * N]
for n in range(N):
    costs.append(list(map(int, input())))

min_reulst[-1] = [costs[-1][0], costs[-1][1], costs[-1][2]]
start = [0, 0, 0]
for k in range(N):
    for i in range(3):
        if costs[k][i] + min_result[k-1][i-1] < costs[k][i] + min_result[k-1][i-2]:
            min_result[k][i] = costs[k][i] + min_result[k-1][i-1]
            if k == 0:
                start[i] = i-1
        elif costs[k][i] + min_result[k-1][i-1] > costs[k][i] + min_result[k-1][i-2]:
            min_result[k][i] = costs[k][i] + min_reulst[k-1][i-2]
            if k == 0:
                start[i] = i-2