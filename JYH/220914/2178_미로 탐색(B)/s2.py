# 2178_미로 탐색(B)
# 2022-09-09

import sys
sys.stdin = open('input.txt', 'r')

def BFS(sti, stj):
    visited = [[0]*M for _ in range(N)]
    q = [] # BFS일 때는 큐 생성
    q.append((sti, stj)) # 시작점 인큐
    visited[sti][stj] = 1
    while q: # 큐에 원소가 있다면
        i, j = q.pop(0) # 디큐
        if i==N-1 and j==M-1:
            return visited[N-1][M-1]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 주변 탐색
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni, nj)) # 인큐
                visited[ni][nj] = visited[i][j] + 1 # 방문 표시

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

print(BFS(0, 0))