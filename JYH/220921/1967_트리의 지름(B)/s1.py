# 1967_트리의 지름(B)
# 2022-09-21

import sys
sys.stdin = open('input.txt', 'r')

def bfs(node):
    global max_node
    global max_value
    q = []
    visited = [0]*(n+1)
    q.append((node, 0)) # node와 value를 함께 저장
    visited[node] = 1

    max_node = 0
    max_value = 0
    while q:
        node, value = q.pop(0)
        for a in range(len(adj_list[node])):
            if visited[adj_list[node][a][0]] == 0:
                q.append((adj_list[node][a][0], value + adj_list[node][a][1]))
                visited[adj_list[node][a][0]] = 1
                if max_value < value + adj_list[node][a][1]:
                    max_value = value + adj_list[node][a][1]
                    max_node = adj_list[node][a][0]
    

n = int(input())
adj_list = [[] for _ in range(n+1)]
for _ in range(n-1):
    par, chi, wei = map(int, input().split())
    adj_list[par].append((chi, wei))
    adj_list[chi].append((par, wei))

bfs(1) # 두번의 bfs
bfs(max_node)
print(max_value)
# 검색해서 풂