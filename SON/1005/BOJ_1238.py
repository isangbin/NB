# BOJ_1238 파티 문제풀이
# 2022-10-05
import heapq

INF = int(1e9)
N, M, X = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))


# 다익스트라
def dijkstra(s, x):
    # 거리 최대값으로 초기화
    distance = [INF] * (N + 1)
    # 최소힙 활용
    q = []
    heapq.heappush(q, (0, s))
    # 시작 distance는 0
    distance[s] = 0
    
    # q에 원소가 남아 있을 때
    while q:
        # q에서 가중치가 최소인 값을 pop 해서 현재 까지 오는 거리랑 지금 위치 저장
        dist, now = heapq.heappop(q)

        # 목적지 도달하면 함수 탈출
        if now == x:
            return dist
        
        # 현재 노드에 저장되어 있는 거리가 q에서 pop한 거리보다 작으면
        # 그냥 while문으로 돌아가기
        if distance[now] < dist:
            continue
        
        # 현재 위치랑 연결된 노드들을 순회하며
        for i in graph[now]:
            # 현재까지 오는데 걸리는 거리에서 다음노드로 가는 가중치 더한 값 저장
            cost = dist + i[1]
            # 해당 저장값이 이미 저장되어 있는 거리보다 작으면
            if cost < distance[i[0]]:
                # distance 저장값을 cost로 초기화 하고
                distance[i[0]] = cost
                # q에 최소힙 push 해주기
                heapq.heappush(q, (cost, i[0]))


answer = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    answer[i] = dijkstra(i, X) + dijkstra(X, i)

print(max(answer))