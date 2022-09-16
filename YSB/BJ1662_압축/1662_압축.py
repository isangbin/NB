import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
prob = list(input())

stack = []
tmp = ''
for i in prob:
    if i != ')':                        # ) 나올때까지 push
        stack.append(i)
    else:                               # 나왔으면
        terminated = True
        tmp = ''
        while terminated:               # 아래 작업을 반복
            a = stack.pop(-1)           # stack맨뒷값 뽑아서
            if a == '(':                # 그게 ( 이면 a는 버리고
                b = stack.pop(-1)       # 한개만 더뽑음
                tmp = int(b) * tmp      # b * 문자열
                for j in str(tmp):      # 연산된 문자열을 다시 stack에 투입
                    stack.append(j)
                terminated = False
            else:
                tmp = a + tmp           # 뽑은게 (가 아니면 tmp에 누적

print(stack)
print(len(stack))
