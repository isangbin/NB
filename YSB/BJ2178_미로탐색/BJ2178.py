import sys

def bfs(i, j, N, M):
    global visited
    visited = [[0] * M for _ in range(N)]
    queue = []
    queue.append((i, j))
    visited[i][j] = 1                                                                           # 방문 표시, 거리 1부터 누적시작
    while queue:                                                                                # queue가 빌 때 까지 무한 반복, 비어버리면 길이없다는 뜻
        i, j = queue.pop(0)
        if i == N-1 and j == M-1:                                                               # 현위치가 맨끝이면
            return visited[i][j]                                                                # 종료하고 현재까지 누적된 거리 반환

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] != '0' and visited[ni][nj] == 0:    # 방문한적없는 열린길이 있으면
                queue.append((ni, nj))                                                          # enqueue
                visited[ni][nj] = visited[i][j] + 1                                             # 여기까지 거리를 누적
    return -1                                                                                   # 길이 막히면 -1출력하게 함

N, M = map(int, sys.stdin.readline().split())
maze = []
for i in range(N):
    tmp = list(str(sys.stdin.readline()))
    tmp.pop(-1)
    maze.append(tmp)


print(bfs(0, 0, N, M))
