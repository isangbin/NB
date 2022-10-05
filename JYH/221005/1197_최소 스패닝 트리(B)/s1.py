# 1197_최소 스패닝 트리(B)
# 2022-10-02

import sys
sys.stdin = open('input.txt', 'r')

# kruskal(find과 union을 사용)
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)
    return

V, E = map(int, input().split())
listC = [] # 간선과 가중치를 닮을 리스트
for _ in range(E):
    A, B, C = map(int, input().split())
    listC.append((A, B, C))
listC.sort(key=lambda x:x[2]) # 가중치가 작은 것부터 sort
p = [i for i in range(V+1)]

total = 0
cnt = 0
for A, B, C in listC:
    if find_set(A) != find_set(B):
        union(A, B)
        total += C
        cnt += 1
        if cnt == V-1:
            break

print(total)
# pypy3로 통과