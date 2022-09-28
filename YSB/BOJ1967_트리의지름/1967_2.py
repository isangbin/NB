import sys

n = int(sys.stdin.readline())

def go(a, b):
    global cnt
    global max_cnt
    cnt += value[a][parent[a]]
    cnt += value[b][parent[b]]
    if parent[a] == parent[b]:
        if max_cnt <= cnt:
            max_cnt = cnt
        return
    else:
        go(parent[a], parent[b])


value = [[0]*(n+1) for _ in range(n+1)]                 # 간선의 가중치
ch1 = [0]*(n+1)
ch2 = [0]*(n+1)
parent = [0]*(n+1)
parent[1] = 1
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
print(grandch)
max_cnt = 0
for i in range(len(grandch)-1):
    for j in range(i+1, len(grandch)):
        cnt = 0
        a = grandch[i]
        b = grandch[j]
        go(a, b)


print(max_cnt)