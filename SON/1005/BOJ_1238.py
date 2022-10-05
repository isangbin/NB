# BOJ_1238 파티 문제풀이
# 2022-10-05
import heapq

INF = int(1e9)
N, M, X = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))


def dijkstra(s, x):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if now == x:
            return dist

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


answer = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    answer[i] = dijkstra(i, X) + dijkstra(X, i)

print(max(answer))