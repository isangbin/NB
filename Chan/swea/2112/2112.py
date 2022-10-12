import sys
sys.stdin = open('input.txt','r')

def testPerformance(A):
    for c in range(W):    # 가로 방향
        cnt = 1    # 시작할 때 1을 카운트
        for r in range(1,D):    # 행 방향으로 모두 탐색
            if A[r][c] == A[r-1][c]:    # 다음 값과 값이 같을 경우
                cnt += 1
            else:   # 다음 값과 값이 다를 경우 cnt를 1로 초기화 한다.
                cnt = 1
            if cnt >= K:    # 만약 cnt가 합격 기준 이상이라면
                break    # 해당 열을 탈출하고 다음 열을 확인한다.
        if cnt < K:    # 해당 열에서 동일한 값이 K 미만이면 불합격
            return False
    return True


# 어떤 막을 몇개 선택할 것인지 조합 함수를 통해 구현
# 최소 1개에서 D개 만큼의 막을 선택

def comb(depth, k, pick): 
    global result
    if depth >= result:    # 최소 약품 주입 회수보다 클 경우 가지치기
        return
    if depth == pick:
        # depth가 뽑아야하는 개수인 pick과 같아졌을 때
        # 합격 기준을 모두 통과했다면
        # result값 갱신
        if testPerformance(film):
            # 최소 약품 주입 횟수 갱신
            result = min(result, depth)
        return

    # 재귀 진행
    # 이부분을 정확히 이해하지 못 하겠음
    for i in range(k,D):
        for d in range(2):
            select.append(i)
            film[i] = drugs[d]
            comb(depth+1, i+1, pick)
            film[i] = raw[i]
            select.pop()


T = int(input())
for tc in range(1,T+1):
    # D: 필름 두께(행), W: 가로 크기(열), K: 합격 기준
    D, W, K = map(int,input().split())
    # 처음 주어지는 필름의 상태
    film = [list(map(int,input().split())) for _ in range(D)]
    # 원래 필름을 복사해둔 상태 / 복원용 리스트
    raw = [f[:] for f in film]
    # 약물을 담은 리스트 / 약품 주입용 리스트
    drugs = [[0]*W, [1]*W]

    if testPerformance(film):    # 약품을 투약하지 않아도 합격기준을 모두 넘길 경우
        result = 0
    else:    # 통과하지 못 했다면 / 투약 필요
        # 최소 약품 주입 횟수
        result = float('inf')
        select = []
        # 막의 개수만큼 반복문 진행
        for pick in range(1,D+1):
            comb(0,0,pick)
            if result < float('inf'):
                # 값이 갱신되면 합격기준을 통과했다는 것이므로 바로 break문으로 나와준다.
                break
    print('#{} {}'.format(tc, result))