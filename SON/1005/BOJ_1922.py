# BOJ_1922 네트워크 연결 문제풀이
# 2022-10-04
import heapq
import collections


def prim(graph, s):
    visited[s] = 1
    next = graph[s]
    heapq.heapify(next)
    weight_sum = 0

    while next:
        weight, u, v = heapq.heappop(next)

        if visited[v] == 0:
            visited[v] = 1
            weight_sum += weight

            for line in graph[v]:
                if visited[line[2]] == 0:
                    heapq.heappush(next, line)
    return weight_sum


N = int(input())
M = int(input())
# lines = [list(map(int, input().split())) for _ in range(M)]
visited = [0] * (N + 1)
graph = collections.defaultdict(list)

for i in range(M):
    u, v, weight = list(map(int, input().split()))
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

print(prim(graph, 1))

