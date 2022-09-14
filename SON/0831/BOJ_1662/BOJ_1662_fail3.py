# BOJ_1662 문제풀이
# 2022-08-27

def com():
    global a
    global stack

    if not a:
        return stack.pop()

    cnt = 0
    while a[-1] == ')':
        a.pop()
        print(a)
        stack.append(0)
        print(stack)

    while a and a[-1] != ')' and a[-1] != '(':
        a.pop()
        print(a)
        cnt += 1
        if not a:
            if stack:
                return(cnt + stack.pop())
            else:
                return(cnt)

    print('hi')
    if a[-1] == ')':
        a.pop()
        print(a)
        stack.append(cnt + stack.pop())
        print(stack)
        return com()
    elif a[-1] == '(':
        a.pop()
        print(a)
        if stack:
            stack.append(int(a.pop()) * (cnt + stack.pop()))
            print(stack)
        else:
            stack.append(cnt * int(a.pop()))
            print(stack)
        if '(' in a:
            stack.append(stack.pop() + stack.pop())
            return com()
        else:
            if a:
                return com()
            else:
                return stack.pop()





a = list(input())
stack = []
print(com())