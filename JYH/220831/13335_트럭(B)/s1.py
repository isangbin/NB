# 13335_트럭(B)
# 2022-08-28

import sys
sys.stdin = open('input.txt', 'r')

n, w, L = map(int, input().split()) # n 트럭수, w 다리길이, L 다리최대하중
weight = list(map(int, input().split())) # 트럭의 무게

q = [0]*w
i = 0
k = 0
while k < n:
    q.pop(0) # pop(0) 먼저하기
    # 큐 안에 있는 무게와 들어갈 무게 합이 L보다 크지 않다면 인큐
    if sum(q) + weight[k] <= L: 
        q.append(weight[k])
        k += 1
    # 크다면 0을 인큐
    else:
        q.append(0)
    i += 1

print(i+w)