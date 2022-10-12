import sys
sys.stdin = open('input.txt','r')
from collections import deque

T = int(input())

tunnel = {
    0: (),    # 그 자리 그대로 
    1: ((1,0),(0,1),(-1,0),(0,-1)),    # 하, 우, 상, 좌
    2: ((1,0),(-1,0)),    # 하, 상
    3: ((0,1),(0,-1)),    # 우, 좌
    4: ((-1,0),(0,1)),    # 상, 우
    5: ((1,0),(0,1)),    # 하, 우
    6: ((1,0),(0,-1)),    # 하, 좌
    7: ((-1,0),(0,-1))    # 상, 좌
}

for tc in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    cnt = 1    # 처음 시작점

    q = deque([(R,C)])    # 시작점을 튜플의 형태로 넣어준다.
    visited[R][C] = 1    # 시작점 방문 처리
    
    # bfs 구현
    while q:
        x, y = q.popleft()
        # tunnel[arr[x][y]] : 어떤 종류의 터널인지
        # dx, dy 
        for dx, dy in tunnel[arr[x][y]]:
            nx, ny = x + dx, y + dy    # nx, ny는 터널을 통해 움직인 좌표값
            if not 0<=nx<N or not 0<=ny<M :    # 범위를 벗어난다면
                 continue
                # 이동한 터널이 이동이 가능했던 곳인지
            if (-dx,-dy) in tunnel[arr[nx][ny]]:
                if not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q += [(nx,ny)]
                    if visited[nx][ny] <= L:
                        cnt += 1
    print('#{} {}'.format(tc,cnt))