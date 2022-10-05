# BOJ_1197 최소 스패닝 트리 문제풀이
# 2022-10-04
def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]


def union(u, v):
    r1 = find_set(u)
    r2 = find_set(v)
    if r1 != r2:
        if rank[r1] > rank[r2]:
            p[r2] = r1
        else:
            p[r1] = r2
            if rank[r1] == rank[2]:
                rank[r2] += 1


def kruskal(edges):
    edges.sort()
    total = 0

    for edge in edges:
        if not edge:
            continue
        weight, u, v = edge
        if find_set(u) != find_set(v):
            union(u, v)
            total += weight

    return total


V, E = map(int, input().split())
p = [0] * (V + 1)
rank = [0] * (V + 1)
edges = [[] for i in range(E + 1)]

for i in range(1, V + 1):
    p[i] = i

for i in range(1, E + 1):
    u, v, weight = map(int, input().split())
    edges[i].extend([weight, u, v])

print(kruskal(edges))