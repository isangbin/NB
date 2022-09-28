# BOJ_1967 트리의 지름 문제푸리
# 2022-09-20
def post(n):
    global max_len
    if n:
        post(ch1[n])
        post(ch2[n])
        if cur_len[ch1[n]] + cur_len[ch2[n]] + length[ch1[n]] + length[ch2[n]] >= max_len:
            max_len = cur_len[ch1[n]] + cur_len[ch2[n]] + length[ch1[n]] + length[ch2[n]]
        cur_len[n] = max(length[ch1[n]] + cur_len[ch1[n]], length[ch2[n]] + cur_len[ch2[n]])


N = int(input())

ch1 = [0 for _ in range(N + 1)]
ch2 = [0 for _ in range(N + 1)]
# par = [0 for _ in range(N + 1)]
length = [0 for _ in range(N + 1)]
cur_len = [0 for _ in range(N + 1)]
max_len = 0

for e in range(N - 1):
    info = list(map(int, input().split()))
    if not ch1[info[0]]:
        ch1[info[0]] = info[1]
    else:
        ch2[info[0]] = info[1]
    # par[info[1]] = info[0]
    length[info[1]] = info[2]

post(1)
print(max_len)