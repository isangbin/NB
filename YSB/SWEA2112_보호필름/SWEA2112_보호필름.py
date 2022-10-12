# tc 46/50 타임오버
import sys
import copy
sys.stdin = open('sample_input.txt', 'r')


def drug(part):
    global ans
    for i in range(1 << len(part)):
        table = copy.deepcopy(film)
        select = []
        for j in range(len(part)):
            if i & (1 << j):
                select.append(part[j])

        for p in part:
            if p in select:
                table[p] = [1]*W
                # print(p, table, len(part), ans)
            else:
                table[p] = [0]*W
                # print(p, table, len(part), ans)
        if len(part) < ans:
            if test(table, K) == 1:
                ans = len(part)


def test(film, K):
    for j in range(W):
        cnt = 0
        for i in range(D-1):
            if film[i][j] == film[i+1][j]:
                cnt += 1
            else :
                cnt = 0

            if cnt == K-1:
                break
        else:
            return 0
    return 1


T = int(input())
for tc in range(1, T+1):
    # D: 세로, W: 가로, K: 통과기준
    D, W, K = map(int, input().split())
    film = []
    for _ in range(D):
        f = list(map(int, input().split()))
        film.append(f)
    # print([[1]*W])
    ans = 10000
    for i in range(1 << D):
        part = []
        for j in range(D):
            if i & (1 << j):
                part.append(j)

        if part:
            if test(film, K) == 1:
                ans = 0
                break

        if len(part) < ans:
            drug(part)

    print('#{} {}'.format(tc, ans))