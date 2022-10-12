# swea_보호필름 문제풀이
# 2022-10-12
from copy import deepcopy


def check(b):
    for j in range(W):
        cnt = 1
        for i in range(D - 1):
            if b[i][j] == b[i + 1][j]:
                cnt += 1
                if cnt >= K:
                    break
            else:
                cnt = 1

            if i == D - 2:
                return False
    return True


def med():
    for i in range(1 << D):
        med_list = []
        for j in range(0, D):
            if i & (1 << j):
                med_list.append(j)
        new_board = deepcopy(board)

        for k in range(1 << len(med_list)):
            for l in range(0, len(med_list)):
                if k & (1 << l):
                    for n in range(W):
                        new_board[med_list[l]][n] = 0
                else:
                    for n in range(W):
                        new_board[med_list[l]][n] = 1

        if check(new_board):
            return len(med_list)


T = int(input())

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]

    print(med())