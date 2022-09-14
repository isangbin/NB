# BOJ_2178 미로 탐색 문제풀이
# 2022-09-13
def bfs(s):                             # 인자는 위치 정보를 가진 list
    global visited
    global cnt
    global start

    visited.append(s)                   # 처음 시작점 방문
    start = 0
    while True:
        end = len(visited)              # 순회 범위 설정을 위한 end
        cnt += 1                        # 한번 방문 시 마다 cnt 증가
        for k in range(start, end):     # 이번 while문에서 start ~ end까지 순회하며
            for i, j in d:
                if visited[k][0] + i == N - 1 and visited[k][1] + j == M - 1:   # 목적지에 도달하면
                    return cnt + 1                                              # 지금까지 센거에 +1 해서 반환 및 탈출

                if 0 <= visited[k][0] + i < N and 0 <= visited[k][1] + j < M:   # 델타 탐색이 판의 범위 안에 있으면
                    if board[visited[k][0] + i][visited[k][1] + j] == 1:        # 해당 위치가 1이면
                        visited.append([visited[k][0] + i, visited[k][1] + j])  # 방문하여 visited에 append하기
                        board[visited[k][0] + i][visited[k][1] + j] = 2         # 판은 2로 바꾸기
        start = end         # 현재의 끝 인덱스가 다음의 시작 인덱스로


N, M = map(int, input().split())


board = [[] for _ in range(N)]  # 판 생성
visited = []                    # 방문 표시 할 공간
start = 0                       # 시작 위치
cnt = 0                         # 몇번 이동했는지 셀 cnt

d = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 델타 탐색

for n in range(N):
    miro = input()
    for i in miro:              # 문제풀이 편이를 위해 int로 변환해 list에 담기
        board[n].append(int(i))

print(bfs([0, 0]))