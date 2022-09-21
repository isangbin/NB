# BOJ_11725 트리의 부모 찾기
# 2022-09-16
import sys
sys.setrecursionlimit(10**6)

def dfs(s):
    while tree[s]:
        p = tree[s].pop()           # 현재 노드와 연결된 값 pop 해서 p에 입력
        tree[p].remove(s)           # 입력 후 연결된 상대 노드의 tree정보에서 현재 노드 연결 제거
        par[p] = s                  # 부모 배열 정보에 입력하기
        dfs(p)                      # dfs로 재귀


N = int(input())

tree = [[] for _ in range(N + 1)]       # 트리 정보 입력 곻간
par = [0 for _ in range(N + 1)]         # 부모 정보 입력 공간

for n in range(N-1):                    # 정점 수 -1 만큼 순회하며
    a, b = map(int, input().split())    # 값 입력
    tree[a].append(b)                   # 누가 부모일지 모르므로 양쪽에 입력
    tree[b].append(a)

dfs(1)
for i in range(2, N+1):
    print(par[i])