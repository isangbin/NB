# swea_1953 탈주범 검거 문제풀이
# 2022-10-12
def search(s):
    visited[s[0]][s[1]] = 1
    q = [s]
    cnt = 1

    while cnt < L:
        cnt += 1
        for i in range(len(q)):
            now = q.pop(0)
            for d in way[board[now[0]][now[1]]]:
                ni, nj = now[0] + d[0], now[1] + d[1]
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] != 0 and visited[ni][nj] == 0:
                    if [d[0] * (-1), d[1] * (-1)] in way[board[ni][nj]]:
                        visited[ni][nj] = 1
                        q.append([ni, nj])


T = int(input())

way = {
        # 우      하       좌       상
    1: [[0, 1], [1, 0], [0, -1], [-1, 0]],
    2: [[-1, 0], [1, 0]],
    3: [[0, 1], [0, -1]],
    4: [[-1, 0], [0, 1]],
    5: [[0, 1], [1, 0]],
    6: [[1, 0], [0, -1]],
    7: [[0, -1], [-1, 0]],
}

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range (N)]
    visited = [[0] * M for _ in range(N)]

    search([R, C])

    result = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                result += 1

    print(f'#{tc} {result}')