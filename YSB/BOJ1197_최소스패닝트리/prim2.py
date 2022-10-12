import sys
input = sys.stdin.readline


def prim(r, V):
    mst = [0]*(V+1)
    mst[r] = 1                          # 시작 정점
    s = 0                               # 가중치의 합

    for _ in range(V):
        u = 0
        minV = 1000001
        for i in range(V+1):            # mst에 포함된 정점 i와 인접한 정점 j중 가중치가 가장 작은 녀석 수색
            if mst[i] == 1:
                for j in range(V+1):
                    if M[i][j] > 0 and mst[j] == 0 and minV > M[i][j]:
                        u = j
                        minV = M[i][j]

        s += minV
        mst[u] = 1
    return s


V, E = map(int, input().split())        # V: 정점수, E: 간선수

M = [[0]*(V+1) for _ in range(V+1)]
L = [[] for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, input().split())
    M[s][e] = w
    M[e][s] = w

print(prim(1, V))