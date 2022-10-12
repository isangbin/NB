# 1953_탈주범 검거
# 2022-10-09

import sys
sys.stdin = open('input.txt', 'r')

def BFS(i, j, t):
    global visited
    q = []
    visited = [[0]*M for _ in range(N)]
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        # 1~7이라면
        if tunnel[i][j] == 1:
            # 다음 좌표가, N X M을 벗어나지 않으면서 연결된 곳이고 방문하지 않았다면, 인큐 및 방문표시
            ni, nj = i, j+1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==6 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i+1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==4 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i, j-1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==4 or tunnel[ni][nj]==5) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i-1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==5 or tunnel[ni][nj]==6) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        elif tunnel[i][j] == 2:
            ni, nj = i+1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==4 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i-1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==5 or tunnel[ni][nj]==6) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        elif tunnel[i][j] == 3:
            ni, nj = i, j+1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==6 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i, j-1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==4 or tunnel[ni][nj]==5) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        elif tunnel[i][j] == 4:
            ni, nj = i, j+1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==6 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i-1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==5 or tunnel[ni][nj]==6) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        elif tunnel[i][j] == 5:
            ni, nj = i, j+1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==6 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i+1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==4 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        elif tunnel[i][j] == 6:
            ni, nj = i, j-1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==4 or tunnel[ni][nj]==5) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i+1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==4 or tunnel[ni][nj]==7) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
        elif tunnel[i][j] == 7:
            ni, nj = i, j-1
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==3 or tunnel[ni][nj]==4 or tunnel[ni][nj]==5) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni, nj = i-1, j
            if 0<=ni<N and 0<=nj<M and (tunnel[ni][nj]==1 or tunnel[ni][nj]==2 or tunnel[ni][nj]==5 or tunnel[ni][nj]==6) and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split()) # N 세로, M 가로, R 세로위치, C 가로위치, L 시간
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    BFS(R, C, L)

    result = 0
    for i in range(N):
        for j in range(M):
            if 1<=visited[i][j]<=L:
                result += 1

    print('#{} {}'.format(tc, result))