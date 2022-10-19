import sys
sys.stdin = open('sample_input.txt', 'r')

# 전선 연결
def connect(idx, cores, board, cnt):
    global core_max, lines

    table = [b[:] for b in board]
    queue = []

    # 모든 코어가 고려되었다면
    if idx == len(cores):
        if cnt > core_max:
            core_max = cnt
            new_lines = 0
            for r in range(N):
                for c in range(N):
                    if table[r][c] == 2:
                        new_lines += 1
            lines = new_lines

        elif cnt == core_max:
            core_max = cnt
            new_lines = 0
            for r in range(N):
                for c in range(N):
                    if table[r][c] == 2:
                        new_lines += 1
            if lines >= new_lines:
                lines = new_lines
        return

    else:
        i, j = cores[idx]

        # 왼쪽으로 연결
        for di in range(0, i):                      # 왼쪽끝까지 순회하면서
            if table[di][j] == 0:                   # 전선 연결 가능하면 2로 표시
                queue.append((di, j))
                table[di][j] = 2
            else:                                   # 전선연결 안되면
                for q in queue:                     # 원상복구 때리고
                    r, c = q
                    table[r][c] = 0
                break                               # 관두기
        else:
            connect(idx+1, cores, table, cnt+1)     # break안당했다 : 코어가 연결됐다
        connect(idx + 1, cores, table, cnt)         # break당했다 : 코어가 연결 안됐다

        # 오른쪽으로 연결
        for di in range(i+1, N-1):
            if table[di][j] == 0:
                queue.append((di, j))
                table[di][j] = 2
            else:
                for q in queue:
                    r, c = q
                    table[r][c] = 0
                break
        else:
            connect(idx+1, cores, table, cnt+1)
        connect(idx + 1, cores, table, cnt)

        # 위로 연결
        for dj in range(0, j):
            if table[i][dj] == 0:
                queue.append((i, dj))
                table[i][dj] = 2
            else:
                for q in queue:
                    r, c = q
                    table[r][c] = 0
                break
        else:
            connect(idx+1, cores, table, cnt+1)
        connect(idx + 1, cores, table, cnt)

        # 아래로 연결
        for dj in range(j, N-1):
            if table[i][dj] == 0:
                queue.append((i, dj))
                table[i][dj] = 2
            else:
                for q in queue:
                    r, c = q
                    table[r][c] = 0
                break
        else:
            connect(idx+1, cores, table, cnt+1)
        connect(idx + 1, cores, table, cnt)

        # 연결 안함
        connect(idx+1, cores, table, cnt)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        b_tmp = list(map(int, input().split()))
        board.append(b_tmp)

    core_cnt = 0        # 벽에 붙은(이미연결된) 코어 수
    core_max = 0        # 그게 아닌 것 중 연결 가능한 최대 코어 수
    lines = 0
    # 코어위치
    cores = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N-1:
                    core_cnt += 1
                else:
                    cores.append((i, j))

    # print(cores)
    cnt = 0
    connect(0, cores, board, cnt)

    core_tot = core_cnt + core_max
    print('#{} {} {}'.format(tc, core_tot, lines))
