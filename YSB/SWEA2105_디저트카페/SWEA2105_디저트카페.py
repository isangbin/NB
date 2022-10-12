import sys
sys.stdin = open('sample_input.txt', 'r')


def turn(a, b):
    if (a, b) == (1, 1):
        return (1, -1)
    elif (a, b) == (1, -1):
        return (-1, -1)
    elif (a, b) == (-1, -1):
        return (-1, 1)
    elif (a, b) == (-1, 1):
        return (1, 1)


def bfs(i, j):
    global ans
    q = []
    ate = []
    q.append((i, j))
    visited[i][j] = 1
    ate.append(cafes[i][j])
    dir_q = [(1, 1)]

    while q:
        ii, jj = q.pop(0)

        while dir_q:
            di, dj = dir_q.pop(0)
            ni = ii + di
            nj = jj + dj
            if ni == i and nj == j:
                if ans < visited[i][j]:
                    ans = visited[i][j]
            else:
                if 0<=ni<N and 0<=nj<N and cafes[ni][nj] not in ate:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append((ni, nj))

            dir_q.append((di, dj))
            dir_q.append(turn(di, dj))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = []
    for _ in range(N):
        c = list(map(int, input().split()))
        cafes.append(c)

    ans = 0
    visited = [[0]*N for _ in range(N)]
    delta = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print('#{} {}'.format(tc, ans))