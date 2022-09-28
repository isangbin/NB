import sys
import copy
input = sys.stdin.readline


def bfs():
    global max_cnt
    visited = [[0]*M for _ in range(N)]
    arr2 = copy.deepcopy(arr)
    q = []
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr2[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))

                visited[ni][nj] = 1
                arr2[ni][nj] = 2

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr2[i][j] == 0:
                cnt += 1
    max_cnt = max(max_cnt, cnt)


def choice(wall_cnt):
    global max_cnt
    if wall_cnt == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    arr[i][j] = 1
                    choice(wall_cnt+1)
                    arr[i][j] = 0


N, M = map(int, input().split())
arr = []
for i in range(N):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

used = [[0]*M for _ in range(N)]

max_cnt = 0
choice(0)
print(max_cnt)
