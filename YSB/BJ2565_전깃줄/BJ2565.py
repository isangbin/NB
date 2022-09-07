import sys

input = sys.stdin.readline

N = int(input())
# idx(0)은 무시한다. idx(1)이 1번라인
lines = [[0]]
for i in range(N):
    a, b = map(int, input().split())
    lines.append([a, b])

lines.sort()
cross = [[] for _ in range(500+1)]      # 인덱스: 줄번호, 내용: 교차하는 줄의 인덱스
crossNum = [[] for _ in range(N+1)]     # 각 줄마다 교차하는 줄의 갯수를 저장

# print(lines, 'lines')

for i in range(1, N+1):                                                     # 각 줄에 대하여
    for j in range(1, N+1):                                                 # 다른 줄들과 비교해서
        if lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]:         # 교차하는경우 cross에 추가
            cross[lines[i][0]].append(lines[j][0])

        elif lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]:
            cross[lines[i][0]].append(lines[j][0])

    crossNum[i] = ([len(cross[lines[i][0]]), lines[i][0]])                  # [교차갯수, 줄번호] 를 모아놓은 리스트

crossNum.sort(reverse=True)                                                 # 교차갯수가 가장 많은줄이 먼저 오게 정렬
# print(cross, 'cross')
# print(crossNum, 'crossNum')

# 제거한 라인 수
cnt = 0

for i in range(N):                          # crossNum을 순회할건데
    cross[crossNum[i][1]] = []               # 맨앞부터 비우고 (줄 제거)
    for a in range(len(cross)):                         # 모든 줄에 대하여
        if crossNum[i][1] in cross[a]:             # i번 줄과 교차했었다면
            cross[a].remove(crossNum[i][1])        # i가 없어졌으니 교차목록에서 제거
            for j in crossNum:
                if j != [] and j[1] == a:
                    j[0] -= 1
    crossNum.sort(reverse=True)
    
    cnt += 1                                # 줄 하나 제거될때마다 cnt 증가
    tmp = 0
    for j in lines:                         # 모든 줄에 대하여
        if cross[j[0]] != []:               # 교차목록이 비어있지 않은게 있으면 다시 돌것임
            tmp = 1
    
    if tmp == 0:                            # 모든 줄의 교차목록이 비어있어서 tmp가 그대로 0이면 그만두고 cnt 출력
        break

print(cnt)