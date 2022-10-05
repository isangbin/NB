# 2178_미로 탐색(B)
# 2022-09-09

import sys
sys.stdin = open('input.txt', 'r')

def DFS(i, j):
    global minV
    if i==N-1 and j==M-1: # [N-1][M-1]에 도착한다면 
        if visited[i][j] < minV:
            minV = visited[i][j]
        return # 완전히 끝나는게 아니라 19번째 줄로 감 
    else: # [N-1][M-1]에 도착하지 않는다면
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = visited[i][j] + 1
                DFS(ni, nj)
                visited[ni][nj] = 0 # 4면이 막혀있으면 그자리를 다시 방문하지 않은 것으로 만들어주기
        return

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]
visited[0][0] = 1 # 시작점 방문한 것으로 표시

minV = N*M # 최단거리
DFS(0,0)
print(minV)
# 시간초과.. BFS로 풀어보자