# BOJ_1012 유기농 배추
# 2022-09-13
import sys
sys.setrecursionlimit(10 ** 4) # 최대 재귀 깊이를 늘려주는 함수


def dfs(n, m):
    global d
    board[n][m] = 2
    for i, j in d:
        # 1을 만나면 dfs로 다 2로 바꿔주기
        if 0 <= n + j < N and 0 <= m + i < M and board[n + j][m + i] == 1:
            dfs(n + j, m + i)


T = int(input())

d =[[0, 1], [1, 0], [0, -1], [-1, 0]]           # 델타 탐색 (우, 하, 좌, 상)

for t in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    # 판 생성
    board = [[0 for _ in range(M)] for _ in range(N)]
    
    # 판 입력 정보
    for k in range(K):
        m, n = map(int, input().split())
        board[n][m] = 1
    
    # 판 전부를 순회하며 1을 만나면 dfs함수 적용
    for n in range(N):
        for m in range(M):
            if board[n][m] == 1:
                # 한번 적용하면 해당 묶음은 모두 2로 바뀌므로
                # 적용할 때 마다 세기
                cnt += 1
                dfs(n, m)

    print(cnt)