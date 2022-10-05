# 10158_개미(B)
# 2022-09-11

import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p+t)//w 
b = (p+t)%w 
if a%2: 
    x = w-b
else:
    x = b

c = (q+t)//h 
d = (q+t)%h 
if c%2: 
    y = h-d
else:
    y = d

print(x, y)
# 구글링.. 답보면 쉬움.. / 시작점에서 t만큼 먼저 가본다는 생각.. 그리고 넓이와 높이로 나눠본다는 생각..