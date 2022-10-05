# 1922_네트워크 연결(B)
# 2022-10-02

import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y): # 부모가 작은 것이 대표원소가 되게 함
    a = find_set(x)
    b = find_set(y)
    if a > b:
        p[a] = b
    else:
        p[b] = a

N = int(input()) # 컴퓨터의 수
M = int(input()) # 선의 수
edge = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
edge.sort()
p = [i for i in range(N+1)]

total = 0
for c, a, b in edge:
    if find_set(a) != find_set(b): # 그냥 부모가 다르면 if문 수행하게 하고 같으면 돌아가게 함(간선수 되면 break하진 않음)
        union(a, b)
        total += c
print(total)