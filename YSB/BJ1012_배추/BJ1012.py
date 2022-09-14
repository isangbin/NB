import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

def dfs(i, j):

    visited[i][j] = 1                                       # 방문 표시
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:              # 4방향 중에
        ni, nj = i+di, j+dj                                 # 
        if 0<= ni < N and 0<= nj < M and stage[ni][nj] == 1 and visited[ni][nj] == 0:     # 그 방향에 방문한적 없는 배추가 붙어있으면
            dfs(ni, nj)                                     # 이동 후 다시 진행
    return

for tc in range(1, T+1):
    M, N, K = map(int, sys.stdin.readline().split())
    cab = [[] for _ in range(K)]
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        cab[i] = [b, a]

    stage = [[0]*M for _ in range(N)]       # 밭
    for i in cab:                           # 배추 심기
        stage[i[0]][i[1]] = 1

    visited = [[0]*M for _ in range(N)]       # 방문정보 저장
    cnt = 0                                 # 배추벌레 수
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and stage[i][j] == 1:     # 현 위치에 방문한적 없는 배추가 있다면
                cnt += 1                                    # 배추벌레 놓고
                dfs(i, j)                                   # dfs로 인접배추 조사및 방문표시

    print(cnt)