# 1012_유기농 배추(B)
# 2022-09-10

import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6) # 깊이를 늘려줌

def DFS(i, j):
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and field[ni][nj]==1 and visited[ni][nj]==0:
            visited[ni][nj] = 1
            DFS(ni, nj)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    answer = 0 # 지렁이수

    visited = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0: # 배추밭이 1이고, 방문하지 않았다면
                visited[i][j] = 1
                DFS(i, j)
                answer += 1

    print(answer)
# 런타임에러, 6번줄로 해결