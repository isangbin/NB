import sys
input = sys.stdin.readline


def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())
edge = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edge.append([s, e, w])

edge.sort(key=lambda x:x[2])
rep = [i for i in range(V+1)]               # 대표원소 배열

cnt = 0         # 선택한 edge 수
total = 0       # mst 가중치의 합

for s, e, w in edge:
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        total += w

        if cnt == V-1:                      # 간선 N-1개를 선택했다면 N개의 정점이 연결된 상태니까 그만함
            break

print(total)