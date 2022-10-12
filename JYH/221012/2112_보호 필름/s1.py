# 2112_보호 필름
# 2022-10-11

import sys
sys.stdin = open('input.txt', 'r')

def film_pass(D, W, K):
    for j in range(W): # 열 순회하며
        for i in range(D-K+1): 
            # 같은 값이 연속으로 K개가 나온다면 break 후 다음열로
            cnt = 1
            for k in range(1, K):
                if film[i][j] == film[i+k][j]:
                    cnt += 1
            if cnt == K:
                break
        # 한 열에서 K개가 나오지 않았다면 그 즉시 열순회도 종료
        else:
            return "non-pass"
            break
    else: # 열 순회를 무사히 마쳤다면 보호필름으로써 합격!
        return 'pass'


def medicine(i, subset, D, W, K): # 행마다 0인 경우 혹은 1인 경우를 확인해야 하므로 재귀 사용
    global result1, answer
    if i == len(subset): # i가 subset 마지막까지 도달했다면(subset에 있는 행을 0이든 1이든 모두 바꿨다면), 보호필름 성능검사 수행  
        result1 = film_pass(D, W, K)
        if result1 == 'pass': # 합격이라면 answer을 기존 answer와 len(subset) 중 더 작은 값으로 바꿈
            answer = min(answer, len(subset))
        return

    if len(subset) > answer: # subset의 길이가 answer보다 크다면 바로 return (가지치기)
        return

    film[subset[i]] = [0]*W # 행을 0으로 바꿨을 때
    medicine(i+1, subset, D, W, K) # 재귀 수행
    film[subset[i]] = [1]*W # 행을 1로 바꿨을 때
    medicine(i+1, subset, D, W, K)
    film[subset[i]] = film_copy[subset[i]] # i가 아니라 subset[i]행임.. 원본 복구


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    film_copy = film[:]

    result = film_pass(D, W, K)
    if result == 'pass': # 약품을 투입하지 않아도 보호필름이 되는 경우
        print('#{} {}'.format(tc, 0))
    else: # 약품을 투입해야 하는 경우
        answer = D # 최종값
        # 행의 수에 따른 부분집합 구하기
        for i in range(1, 1<<D):
            subset = []
            for j in range(D):
                if i & (1<<j):
                    subset.append(j)
            # 부분집합을 구한 후, 그 행들이 0 혹은 1로 바꿨을 때 보호필름 성능검사 합격할 수 있는지 확인
            medicine(0, subset, D, W, K)
            
        print('#{} {}'.format(tc, answer))