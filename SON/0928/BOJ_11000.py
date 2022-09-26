# BOJ_11000 강의실 배정 문제풀이
# 2022-09-25
import sys
import heapq

input = sys.stdin.readline

N = int(input())

classes = [list(map(int, input().split())) for _ in range(N)]   # 수업 정보
classes.sort(key=lambda x: x[0])                                # 수업 시작 시간을 오름차순으로 정렬

q = []
for n in range(N):
    if q and classes[n][0] >= q[0]:                             # 수업 시작 시간이 heap의 가장 빠른 종료시간 보다 크거나 같으면
        heapq.heappop(q)                                        # 해당 값을 pop 하고
        heapq.heappush(q, classes[n][1])                        # 힙에 추가
    else:
        heapq.heappush(q, classes[n][1])                        # 가장 빠른 종료시간 보다 작으면 새롭게 heap에 추가

print(len(q))