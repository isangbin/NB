# BOJ_1753 최단경로 문제풀이
# 2022-10-05
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
INF = int(1e9)
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))


def dijkstra(s):
    global distance

    distance = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])