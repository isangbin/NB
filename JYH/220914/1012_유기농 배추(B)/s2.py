# 1012_유기농 배추(B)
# 2022-09-10

import sys
sys.stdin = open('input.txt', 'r')

def BFS(i, j):
    global answer
    q.append((i, j)) # 인큐
    visited[i][j] = 1 # 방문표시
    while q: # 큐에 원소가 남아있다면
        i, j = q.pop(0) # 디큐
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 주변 탐색
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and field[ni][nj]==1 and visited[ni][nj]==0: # 방문하지 않았다면
                q.append((ni, nj)) # 인큐
                visited[ni][nj] = 1 # 방문표시
    answer += 1 # 인접한 곳은 방문표시 해주고 더 이상 인접한 곳이 없다면 answer을 +1해줌

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    
    answer = 0 # 지렁이수
    visited = [[0]*M for _ in range(N)] # 아래에서 visited를 사용하기에 함수 밖에서 정의함 
    q = []

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and visited[i][j] == 0: # 배추밭이 1이고, 방문하지 않았다면
                BFS(i, j) # BFS 수행하기

    print(answer)