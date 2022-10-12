# BOJ_1922 네트워크 연결 문제풀이
# 2022-10-04
import heapq
import collections

# 프림
def prim(graph, s):
    # 출발점 방문 표시
    visited[s] = 1
    # 출발점과 연결된 노드들이 다음 후보
    next = graph[s]
    # heap화 하기
    heapq.heapify(next)
    weight_sum = 0

    # 다음 노드가 있는 동안
    while next:
        # 최소힙 pop 해서 정보 저장
        weight, u, v = heapq.heappop(next)

        # 해당노드를 방문한 적이 없으면
        if visited[v] == 0:
            # 방문표시하고
            visited[v] = 1
            # 가중치 더하기
            weight_sum += weight

            # 해당 노드와 연결된 간선들 중 방문하지 않은 노드가 있으면
            for line in graph[v]:
                if visited[line[2]] == 0:
                    # 힙에 넣기
                    heapq.heappush(next, line)
    return weight_sum


N = int(input())
M = int(input())
visited = [0] * (N + 1)
graph = collections.defaultdict(list)

for i in range(M):
    u, v, weight = list(map(int, input().split()))
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

print(prim(graph, 1))

