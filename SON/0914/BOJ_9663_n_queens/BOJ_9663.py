# BOJ_9663 N-Queen 문제풀이
# 2022-09-13
def queen(i):
    global cnt

    if i == N:              # 판의 끝에 도달 하면
        cnt += 1            # 퀸을 다 놓은 것 이므로 세기
        return

    for j in range(N):
        if col[j] == 0 and dig1[i+j] == 0 and dig2[j - i + N - 1] == 0:     # 세로, 두 대각선 모두 0이면
            col[j] = 1                                                      # 각각의 값들을 1로 초기화 한 후
            dig1[i+j] = 1
            dig2[j - i + N - 1] = 1

            queen(i+1)                                                      # 다음 줄로 queen함수 돌리기

            col[j] = 0                                                      # 돌리고 나오면 backtracking
            dig1[i + j] = 0
            dig2[j - i + N - 1] = 0


N = int(input())
col = [0 for _ in range(N)]             # 세로에 놓을 수 있는지 정보 저장을 위해
dig1 = [0 for _ in range(2 * N - 1)]    # 대각선
dig2 = [0 for _ in range(2 * N - 1)]    # 대각선

cnt = 0
queen(0)
print(cnt)