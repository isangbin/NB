import sys
input = sys.stdin.readline


def dijk(start):
    used = [start]
    D[start] = 0
    for v in range(V+1):
        D[v] = roads[start][v]

    while len(used) != V:
        small = float('INF')
        small_idx = 0
        for i in range(V+1):
            if i not in used and D[i] < small:
                small = D[i]
                small_idx = i
        if small == float('INF'):
            return -1
        else:
            used.append(small_idx)

        for v in range(V+1):
            D[v] = min(D[v], D[small_idx] + roads[small_idx][v])

    return 1

V, E = map(int, input().split())    # V: 정점 개수, E: 간선 개수
K = int(input())                    # K: 시작 정점

roads = [[float('INF')]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    roads[u][v] = w

D = [float('INF')]*(V+1)
ans = dijk(K)

for i in range(1, V+1):
    if i == K:
        print(0)
    elif D[i] == float('INF'):
        print('INF')
    else:
        print(D[i])