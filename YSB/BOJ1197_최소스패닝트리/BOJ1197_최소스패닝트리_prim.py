import sys
input = sys.stdin.readline


def prim(r, V):
    mst = [0]*(V+1)                     # mst에 들어갔는지
    key = [1000001]*(V+1)               # 가중치 초기값 = 무한대
    key[0] = 0                          # 0번 정점은 없으므로 0으로 둠
    key[r] = 0                          # 시작점의 key는 0
    
    for _ in range(V):                  # 정점을 V번 선택함
        u = 0
        minV = 1000001
        for i in range(V+1):            # key가 최소인 정점 u를 수색
            if mst[i] == 0 and key[i] < minV:
                u = i
                minV = key[i]
        mst[u] = 1                      # 정점 u는 mst에 연결됨

        for v in range(V+1):
            if mst[v] == 0 and M[u][v] > 0:
                key[v] = min(key[v], M[u][v])
    print(key)
    return sum(key)


V, E = map(int, input().split())        # V: 정점수, E: 간선수

M = [[0]*(V+1) for _ in range(V+1)]
L = [[] for _ in range(V+1)]
for i in range(E):
    s, e, w = map(int, input().split())
    M[s][e] = w
    M[e][s] = w

print(prim(1, V))