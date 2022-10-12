import sys
sys.stdin = open('sample_input.txt', 'r')


def where_I_am(i, j):
    if tunnel[i][j] == 1:
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]
    elif tunnel[i][j] == 2:
        return [(1, 0), (-1, 0)]
    elif tunnel[i][j] == 3:
        return [(0, 1), (0, -1)]
    elif tunnel[i][j] == 4:
        return [(-1, 0), (0, 1)]
    elif tunnel[i][j] == 5:
        return [(1, 0), (0, 1)]
    elif tunnel[i][j] == 6:
        return [(1, 0), (0, -1)]
    elif tunnel[i][j] == 7:
        return [(-1, 0), (0, -1)]


def valid_check(di, dj, ni, nj):
    if di == 1:
        if tunnel[ni][nj] in [1, 2, 4, 7]:
            return 1
    elif di == -1:
        if tunnel[ni][nj] in [1, 2, 5, 6]:
            return 1
    elif dj == 1:
        if tunnel[ni][nj] in [1, 3, 6, 7]:
            return 1
    elif dj == -1:
        if tunnel[ni][nj] in [1, 3, 4, 5]:
            return 1
    else:
        return 0


def bfs(R, C, L):
    q = []
    q.append((R, C))
    visited[R][C] = 1

    while q:
        i, j = q.pop(0)
        if visited[i][j] == L:
            continue
        else:
            for di, dj in where_I_am(i, j):
                ni = i + di
                nj = j + dj
                if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and valid_check(di, dj, ni, nj) == 1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))


T = int(input())
for tc in range(1, T+1):
    # N:세로, M:가로, (R, C):맨홀, L:소요시간
    N, M, R, C, L = map(int, input().split())
    tunnel = []
    for _ in range(N):
        t = list(map(int, input().split()))
        tunnel.append(t)

    visited = [[0] * M for _ in range(N)]
    bfs(R, C, L)
    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 0:
                cnt += 1
    print('#{} {}'.format(tc, cnt))