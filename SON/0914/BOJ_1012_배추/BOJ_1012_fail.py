# BOJ_1012 유기농 배추
# 2022-09-11

T = int(input())

d =[[0, 1], [1, 0], [0, -1], [-1, 0]]

for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    board = [[0 for _ in range(M)] for _ in range(N)]

    for k in range(K):
        m, n = map(int, input().split())
        board[n][m] = 1

    for n in range(N):
        for m in range(M):
            flag = 0
            if board[n][m] == 1:
                for i, j in d:
                    if 0 <= n + j < N and 0 <= m + i < M:
                        if board[n + j][m + i] == 2:
                            board[n][m] = 2
                            flag = 1
                            break
                if flag == 0:
                    cnt += 1
                    board[n][m] = 2

    print(cnt)