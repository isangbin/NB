# 1753_최단경로(B)
# 2022_10_02

import sys
sys.stdin = open('input.txt', 'r')

import heapq

def dijkstra(k):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 인큐
    heapq.heappush(q, (0, k))
    d[k] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, weight in adjL[now]:
            cost = dist + weight
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < d[next_node]:
                d[next_node] = cost
                heapq.heappush(q, (cost, next_node))    


V, E = map(int, input().split()) # V:정점개수(1~V) / E:간선개수
K = int(input()) # 시작정점 번호
adjL = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adjL[u].append((v, w))

d = [10*20000*300000]*(V+1)
dijkstra(K)
for m in range(1, V+1):
    if m == K:
        print(0)
    elif d[m] == 10*20000*300000:
        print('INF')
    else:
        print(d[m])


# 시간초과.. 우선순위큐를 이용해줘야 한단다.. heap
# def dijkstra(k):
#     U = [k]
#     for i in range(len(adjL[k])): # 시작점에서 인접한 거리 정보를 d에 넣기
#         d[adjL[k][i][0]] = adjL[k][i][1]
#     for j in range(V-1): # U와 V가 같아질 때까지
#         x = 0 # U에 포함되지 않고 d에서 가장 작은 값 선택
#         for l in range(1, V+1):
#             if (l not in U) and d[l] < d[x]:
#                 x = l
#         U.append(x)
#         for y in range(len(adjL[x])): # x에 인접한 정점 거리 + d[x]와 d[y]에서 최소값을 넣어주기
#             d[adjL[x][y][0]] = min(d[adjL[x][y][0]], adjL[x][y][1]+d[x])


# V, E = map(int, input().split()) # V:정점개수(1~V) / E:간선개수
# K = int(input()) # 시작정점 번호
# adjL = [[] for _ in range(V+1)]
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjL[u].append((v, w))

# d = [10*20000*300000]*(V+1)
# dijkstra(K)
# for m in range(1, V+1):
#     if m == K:
#         print(0)
#     elif d[m] == 10*20000*300000:
#         print('INF')
#     else:
#         print(d[m])


# 메모리 초과.. 인접행렬 말고 리스트로 풀기
# def dijkstra(k):
#     U = [k] # U 생성 후 k 넣기
#     for i in range(V+1): # k에 인접한 거리를 d에 넣기
#         d[i] = adjM[k][i]

#     for j in range(V-1): # U가 V랑 같을 때까지
#         x = 0
#         for l in range(1, V+1): # U에 포함되지 않고 d에서 가장 작은 값 선택
#             if (l not in U) and d[l] < d[x]:
#                 x = l
#         U.append(x) # U에 append
#         for y in range(1, V+1): # d[x]+바뀐 x에 인접한 거리와 d[y] 중 작은 값으로 d 갱신(1부터)
#             if 0<adjM[x][y]<10*20000*300000:
#                 d[y] = min(d[y], d[x]+adjM[x][y])


# V, E = map(int, input().split()) # V:정점개수(1~V) / E:간선개수
# K = int(input()) # 시작정점 번호
# adjM = [[10*20000*300000]*(V+1) for _ in range(V+1)]
# for i in range(V+1): # 0,0부터 해도 무방
#     adjM[i][i] = 0

# for _ in range(E):
#     u, v, w = map(int, input().split())
#     adjM[u][v] = w # 단방향

# d = [10*20000*300000]*(V+1)
# dijkstra(K)
# for m in range(1, V+1):
#     if m == K:
#         print(0)
#     elif d[m] == 10*20000*300000:
#         print('INF')
#     else:
#         print(d[m])