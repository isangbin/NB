# 11725_트리의 부모 찾기(B)
# 2022-09-16

import sys # 이거 안해서 NameError남
sys.stdin = open('input.txt', 'r')

def bfs(s):
    global visited
    q = []
    visited = [0]*(N+1)
    q.append(s)
    visited[s] = 1
    while q:
        i = q.pop(0)
        # 해야할 것
        for j in L[i]: # 인접하면서 방문하지 않았다면 인큐
            if visited[j] == 0:
                q.append(j)
                visited[j] = visited[i] + 1


N = int(sys.stdin.readline()) # 노드 개수
L = [[] for _ in range(N+1)] # 정점을 인덱스로 한 2차원 리스트
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split()) # 연결된 두 정점
    L[a].append(b)
    L[b].append(a)
# L : [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

# bfs를 하고, 1. 연결되어 있는 것 중 2. visited가 나보다 하나 작다면 부모! (시간초과 방지)
bfs(1) # 시작점 = 1

# visited : [0, 1, 3, 3, 2, 4, 2, 3]
for k in range(2, N+1):
    for l in range(len(L[k])):
        if visited[L[k][l]] == visited[k]-1:
            answer = L[k][l]
            break
    print(answer)