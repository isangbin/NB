# 14502_연구소(B)
# 2022-09-26

import sys
sys.stdin = open('input.txt', 'r')

def BFS():
    q = []
    visited = [[0]*M for _ in range(N)]
    for i in range(N): # 초기 바이러스 있는 좌표 구해서 인큐
        for j in range(M):
            if virus[i][j] == 2:
                q.append((i, j))
                visited[i][j] = 1
    while q: # 바이러스 퍼뜨리기
        i, j = q.pop(0)
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0 and virus[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1

    cnt_no_virus = 0 # 바이러스 없는 개수 구해서 return (visited 0이고(바이러스가 퍼지지 않은 곳) virus도 0인 곳(벽이 아닌 곳))
    for i in range(N):
        for j in range(M):
            if visited[i][j]==0 and virus[i][j]==0:
                cnt_no_virus += 1
    return cnt_no_virus

# 벽 3개 세우기
def makewall(cnt):
    global result
    if cnt == 3:
        answer = BFS() # 3개 세운 후 BFS 수행
        if result < answer:
            result = answer
        return # return 꼭!!

    for i in range(N): # 재귀를 하게되면 다시 돌아와서 그 다음거 수행할 수 있게 됨
        for j in range(M):
            if virus[i][j] == 0:
                virus[i][j] = 1
                makewall(cnt+1)
                virus[i][j] = 0
            
N, M = map(int, input().split())
virus = [list(map(int, input().split())) for _ in range(N)]

result = 0
makewall(0)
print(result)