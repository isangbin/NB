import sys
N = int(sys.stdin.readline())

def cut(a):
    if a == 51:
        return
    for j in ch1[a]:
        cut(j)

    ch1[a] = [51]


parent = list(map(int, sys.stdin.readline().split()))

ch1 = [[]*N for _ in range(N)]

for i in range(N):
    if parent[i] == -1:
        pass
    else:
        ch1[parent[i]].append(i)

delete = int(sys.stdin.readline())

cut(delete)
cnt1 = 0
for i in ch1:
    if i == [] or i == [delete]:
        cnt1 += 1

print(cnt1)