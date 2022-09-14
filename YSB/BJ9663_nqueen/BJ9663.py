import sys

def check(i, N):
    global cnt
    global queens
    for j in range(N):                                                  # i번째 줄의 각 자리에 대하여
        for queen in queens:
            if j == queen[1] or abs(i-queen[0]) == abs(j-queen[1]):     # 다른 퀸에 잡히는 자리면 유망하지 X
                break
        else:                                                           # 안잡히는 자리면 유망하므로 이하를 진행
            if i == N-1:                                                # 지금 위치가 마지막 줄인 경우
                cnt += 1                                                # 경우에 만족했으므로 cnt +1 후 경우의 수 1개 종료
                queens.append([i, j])
                print(queens, cnt)
                return
            else:                                                       # 마지막 줄이 아닌 경우
                queens.append([i, j])                                   # 유망하다고 판명된 현 위치에 퀸을 놓고
                print(queens, cnt)
                # i += 1                                                # 다음 줄에 대해
                check(i+1, N)                                           # 다시 유망한 자리가 있는지 조사 시작
    # queens.pop(-1)

N = int(sys.stdin.readline())
chess = [[0]*N for _ in range(N)]
queens = []
cnt = 0     # 경우의 수

i = 0
for j in range(N):              # 첫째 줄의 각 자리에
    queens.append([i, j])       # 퀸을 놓아보고
    check(i+1, N)               # 가능한 경우의 수 탐색
    queens = []
print(cnt)