import sys

n = int(sys.stdin.readline())


def bfs(i):
    global cnt
    global max_cnt
    visited[i] = 1
    if i in grandch:
        if max_cnt <= cnt:
            max_cnt = cnt
        cnt = 0

    else:
        if parent[i] != 'root' and visited[parent[i]] == 0:
            cnt += value[i][parent[i]]
            print(cnt, i, 1)
            print(visited)
            bfs(parent[i])
        if visited[ch1[i]] == 0:
            cnt += value[i][ch1[i]]
            print(cnt, i, 2)
            print(visited)
            bfs(ch1[i])
        if visited[ch2[i]] == 0:
            cnt += value[i][ch2[i]]
            print(cnt, i, 3)
            print(visited)
            bfs(ch2[i])


value = [[0]*(n+1) for _ in range(n+1)]                 # 간선의 가중치
ch1 = [0]*(n+1)
ch2 = [0]*(n+1)
parent = [0]*(n+1)
parent[1] = 'root'
for i in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    value[a][b] = c
    value[b][a] = c
    parent[b] = a
    if ch1[a] == 0:
        ch1[a] = b
    else:
        ch2[a] = b

grandch = []
for i in range(1, n+1):
    if ch1[i] == 0:         # 맨 아래에있는 노드를 모음
        grandch.append(i)
print('value', value)
print('parent', parent)
print('ch1', ch1)
print('ch2', ch2)
print('grandch', grandch)


max_cnt = 0
for i in grandch:
    cnt = 0
    visited = [0]*(n+1)
    visited[i] = 1
    cnt += value[i][parent[i]]
    bfs(parent[i])

print(max_cnt)
