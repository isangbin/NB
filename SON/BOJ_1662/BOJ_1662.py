# BOJ_1662 문제풀이
# 2022-08-27
import sys
def com():
    # 숫자 세기
    cnt = 0
    # 남은 문자열 없으면 stack에 남은거 반환, 탈출
    if not a:
        return stack.pop()
    # 괄호 없이 숫자들만 문자열에 남아 있으면
    elif '(' not in a:
        # stack에 남은게 있으면 스택에 있는거 더해서 반환, 탈출
        if stack:
            return stack.pop() + len(a)
        # 아니면 그냥 반환 (처음 입력이 '123' 이런거 일 때), 탈출
        else:
            return len(a)

    # 세가지 경우
    # 1. ')' 이면 다시 돌기
    if a[-1] == ')':
        # 괄호 제거 하고(이하 동문)
        a.pop()
        # 스택에 0 삽입 하고 재귀 돌기
        stack.append(0)
        return com()
        # 돌고 나오면 스택에 쌓여 있던 거랑 재귀 돌고 쌓인거 합해서 다시 넣기
        stack.append(stack.pop() + stack.pop())

    # 2. 숫자 이면 괄호 나올때 까지 세기
    while a[-1] != ')' and a[-1] != '(':
        a.pop()
        cnt += 1

    # 숫자 다 세고 ( 가 아니라 ) 가 나오면
    if a[-1] == ')':
        if stack:
            # 센거랑 스택에 쌓여있던거 더해서 넣고 다시 재귀
            stack.append(cnt + stack.pop())
            return com()
        # 스택에 쌓인거 없으면 그냥 재귀
        else:
            stack.append(cnt)
            return com()
    # 3. ( 이면
    else:
        a.pop()
        # 괄호 앞 숫자 * (이번에 센 숫자 + 현재 괄호 에서 쌓인거) 스택에 넣기
        stack.append(int(a.pop()) * (cnt + stack.pop()))
        # 마지막 괄호 벗기기가 아니면 스택에 2개 이상 쌓여 있으므로 현재 푼 괄호랑 스택하나 합쳐서 다시 넣기
        if len(stack) >= 2:
            stack.append(stack.pop() + stack.pop())
    # 재귀
    return com()


a = list(sys.stdin.readline())
a.pop()
stack = []
print(com())