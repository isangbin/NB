# BOJ_17298 오큰수
# 2022-08-26

N = int(input())

board = list(map(int, input().split()))
stack = [0]
# 오큰수 못찾은 곳 -1 로 출력하기 위해 모두 -1로 초기화
result = [-1 for _ in range(N)]
i = 1

# stack
# i가 N보다 작을때 까지
while stack and i < N:
    # 현재 인덱스가 stack에 쌓여있는 인덱스 보다 크면
    while stack and board[stack[-1]] < board[i]:
        # 현재 인덱스 값을 결과 스택에 추가
        result[stack[-1]] = board[i]
        # 오큰수를 찾았으니깐 pop
        stack.pop()

    stack.append(i)
    i += 1

for i in result:
    print(i, end=" ")