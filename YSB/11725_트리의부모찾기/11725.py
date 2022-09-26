import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())


def dfs(root):
    for i in connect[root]:
        if parent[i] == 0:
            parent[i] = root
            dfs(i)


ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
parent = [0]*(N+1)
connect = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    connect[a].append(b)
    connect[b].append(a)
print(connect)
parent[1] = 'root'
dfs(1)

for i in range(2, N+1):
    print(parent[i])