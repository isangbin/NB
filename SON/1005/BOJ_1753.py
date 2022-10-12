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


# 다익스트라
def dijkstra(s):
    global distance

    # 최대값으로 초기화
    distance = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    # q에 저장되어 있는 값이 있는 동안
    while q:
        dist, now = heapq.heappop(q)

        # 저장되어 있는 현재 노드까지 오는 거리가 최소힙에서 pop한 값보다 작으면
        # 뒷부분 진행하지 않고 다시 while문
        if distance[now] < dist:
            continue

        # 현재 노드랑 연결되어 있는 노드 순회하며
        for i in graph[now]:
            # 현재 노드까지의 거리와 현재 노드에서 순회 노드까지 거리를 더한 값이
            cost = dist + i[1]
            # 이미 저장되어 있는 순회한 노드까지의 거리보다 작으면
            if cost < distance[i[0]]:
                # 거리 초기화 하고
                distance[i[0]] = cost
                # heappush
                heapq.heappush(q, (cost, i[0]))


dijkstra(K)

for i in range(1, V+1):
    # 한번도 거리가 저장되지 않으면 경로 없음
    if distance[i] == INF:
        print('INF')
    # 값이 저장되어 있으면 최소 거리 출력
    else:
        print(distance[i])