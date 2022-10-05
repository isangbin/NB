# 9663_N-Queen(B)
# 2022-09-11

import sys
sys.stdin = open('input.txt', 'r')

def is_promising(v): # 유망한지 판단
    for m in range(v):
        if row[m] == row[v]: # 세로줄 판단 / v행 이전 행 중의 하나가 row[v]랑 같다면 0 리턴
            return 0
        if abs(row[m]-row[v]) == abs(m-v): # 대각선 판단 / y축차이 = x축차이
            return 0
    return 1


def n_queens(i):
    global answer
    # 마지막 행에 도착
    if i == N:
        answer += 1
        return

    else:
        for j in range(N): # i행에서 j열을 0부터 N-1까지 옮겨가면서 유망한 곳 찾기
            row[i] = j # 1차원 배열로 생각해보기
            if is_promising(i): # 유망하면 다음행 확인하고자 재귀 수행
                n_queens(i+1)

N = int(input())
row = [0]*N

answer = 0 # 경우의 수
n_queens(0)
print(answer)
# 구글링.. 파이파이로 해야함..