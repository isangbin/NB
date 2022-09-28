# BOJ_1662 문제풀이
# 2022-08-27

def com():
    global a
    global stack
    cnt = 0
    if not a:
        return sum(stack)

    if a[-1] == ')':
        a.pop()
        print(stack)
        return com()

    while a[-1] != ')' and a[-1] != '(':
        a.pop()
        cnt += 1
    stack.append(cnt)
    print(stack)

    if a[-1] == '(':
        a.pop()
        stack.append(int(a.pop()) * stack.pop() + stack.pop())
        print(stack)
        return


a = list(input())
stack = []
print(com())