# 2578_빙고(B)
# 2022-08-27

import sys
sys.stdin = open('input.txt', 'r')

cheolsu = [list(map(int, input().split())) for _ in range(5)]
moderator = []
for _ in range(5):
    moderator += list(map(int, input().split())) # moderator = [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]

for k in range(25):
    check_i = -1
    check_j = -1
    for i in range(5):
        for j in range(5):
            if moderator[k] == cheolsu[i][j]:
                check_i, check_j = i, j
                cheolsu[check_i][check_j] = 0
                break
        if check_i != -1:
            break

    bingo = 0
    cnt_x = 0 # 대각선!!
    cnt_xrev= 0
    for m in range(5):
        cnt_row = 0 # 가로
        cnt_col = 0 # 세로
        for n in range(5):
            if cheolsu[m][n] == 0:
                cnt_row += 1
            if cheolsu[n][m] == 0:
                cnt_col += 1
            if m == n:
                if cheolsu[m][n] == 0:
                    cnt_x += 1
            if m + n == 4:
                if cheolsu[m][n] == 0:
                    cnt_xrev += 1
            if cnt_row == 5:
                bingo += 1
            if cnt_col == 5:
                bingo += 1
    # 아예 for문 밖에서 해야함!! 초기화를 맨 위에서 한 번만 하다보니 만약 대각선이 빙고가 되면 for문 돌 때마다 cnt_xrev 하나씩 올라감
    if cnt_x == 5: 
        bingo += 1
    if cnt_xrev == 5:
        bingo += 1
    
    if bingo >= 3: # 2개에서 4개가 되는 경우가 있으니..... 정수님 풀이 보고 영감 얻음..
        break
print(k+1)