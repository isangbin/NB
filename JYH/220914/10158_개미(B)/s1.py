# 10158_개미(B)
# 2022-09-11

import sys
sys.stdin = open('input.txt', 'r')

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

di = -1
dj = 1

time = 1
while time <= t:
    ni, nj = (h-q)+di, p+dj

    if (nj==w and ni==0) or (ni==h and nj==0):
        di = -(di) 
        dj = -(dj)
    elif nj==w or nj==0:
        dj = -(dj)
    elif ni==0 or ni==h:
        di = -(di)
    
    q = h-ni
    p = nj
    time += 1

print(p, q)
# 시간초과..