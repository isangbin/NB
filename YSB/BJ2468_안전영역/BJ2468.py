import sys
N = int(sys.stdin.readline())
area = []
for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    area.append(tmp)

print(area)