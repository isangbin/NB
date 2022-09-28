# BOJ_17404 RGB 거리 2
# 2022-09-04
import sys

N = int(input())

# 색칠 비용 담을 공간
costs = []
# 정답을 최대값으로 초기화 해놓기
ans = sys.maxsize
# 입력
for n in range(N):
    costs.append(list(map(int, input().split())))
# 첫번째 집의 색을 빨강으로 칠했을때, 초록으로 칠했을때, 파랑으로 칠했을 때를 나눠서 생각
for i in range(3):
    # 결과값은 매번 시작할때 마다 최대값으로 초기화
    min_result = [[sys.maxsize, sys.maxsize, sys.maxsize] for _ in range(N)]
    # 그 후 시작 색만 값을 주어 해당 색으로 시작 했을 때 만 유의미 하게
    min_result[0][i] = costs[0][i]
    # 각각의 색깔 별로 본인 색을 제외한 이전 색 중 최소인 값을 더 해 저장 
    for j in range(1, N):
        min_result[j][0] = costs[j][0] + min(min_result[j - 1][2], min_result[j - 1][1])
        min_result[j][1] = costs[j][1] + min(min_result[j - 1][0], min_result[j - 1][2])
        min_result[j][2] = costs[j][2] + min(min_result[j - 1][0], min_result[j - 1][1])
    
    # 최종 색 중 시작할 때의 색 i 와 같지 않은 값 중 최솟값을 ans에 저장
    for j in range(3):
        if i != j:
            ans = min(ans, min_result[-1][j])

print(ans)