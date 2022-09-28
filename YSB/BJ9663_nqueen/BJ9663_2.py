import sys

# 유망한지 조사
def promising(x):
    for i in range(x):                                                  # 현재행 위의 모든 행의 퀸들에 대하여
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):      # 현재행 퀸과 같은 열에 있거나, 대각선상에 놓인 것이 있는 경우
            return False                                                # 유망하지 않음
    return True                                                         # 모든 퀸에 대해 적발되지 않았다면 유망함

# 퀸 놓기
def nqueen(x):
    global cnt
    if x == N:                  # 마지막줄까지 퀸이 놓인 후면 cnt +1
        cnt += 1
        return
    else:
        for i in range(N):      # 마지막줄이 아니라면
            row[x] = i          # x번째 행의 i번째 열에 퀸을 놓고,
            if promising(x):    # 유망하다면
                nqueen(x+1)     # 다음 행에서 작업 반복, 유망하지 않다면 그냥 거기서 추가작업 없이 끝(백트래킹)


N = int(sys.stdin.readline())

row = [0]*N                                     # idx는 퀸이 놓인 행, 그 값은 열을 의미.  
cnt = 0                                         # 경우의 수

nqueen(0)
print(cnt)
