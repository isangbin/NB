# BOJ_1967 트리의 지름 문제풀이
# 2022-09-20
import sys
sys.setrecursionlimit(10**6)
def post(n):
    global max_len
    global cur_len
    global length
    if n:
        for i in ch[n]:
            post(i)

        max_list = []
        for i in ch[n]:
            max_list.append(length[i] + cur_len[i])

        if max_list:
            max_list.sort()
            cur_len[n] = max_list.pop()

            if max_list:
                if cur_len[n] + max_list[-1] >= max_len:
                    max_len = cur_len[n] + max_list[-1]
    return


N = int(input())

ch = [[] for _ in range(N + 1)]

# par = [0 for _ in range(N + 1)]
length = [0 for _ in range(N + 1)]
cur_len = [0 for _ in range(N + 1)]
max_len = 0

for e in range(N - 1):
    info = list(map(int, input().split()))
    ch[info[0]].append(info[1])
    # par[info[1]] = info[0]
    length[info[1]] = info[2]

post(1)
print(max_len)