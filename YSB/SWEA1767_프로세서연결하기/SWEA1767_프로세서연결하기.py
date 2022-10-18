import sys
sys.stdin = open('sample_input.txt', 'r')

# 전선 연결
def connect(i, j):
    pass


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        b_tmp = list(map(int, input().split()))
        board.append(b_tmp)

    core_cnt = 0
    # 코어위치
    cores = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    core_cnt += 1
                else:
                    cores.append((i, j))

