# 1662_압축(B)
# 2022-08-30

import sys
sys.stdin = open('input.txt', 'r')

S = input()
stack = []

for s in S:
    if s != ')':
        stack.append(s)
    # ')' 만나면 '(' 나올 때까지 pop해서 tmp_string에 넣기
    else:
        tmp_string = ''
        while stack:
            a = stack.pop() # 미리 설정해주기, 아래에서 stack.pop() 쓸 때마다 pop됨
            if a != '(':
                tmp_string += a
            else:
                # 하나 더 pop해서 숫자로 만든 후, tmp_string과 곱한 후 결과값 push
                stack.extend(int(stack.pop()) * tmp_string) # extend로 넣어주면 '79'가 '7', '9' 따로따로 stack에 들어감
                break

print(len(stack))
# 메모리 초과..