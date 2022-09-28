# BOJ_1662 문제풀이
# 2022-08-27

def com():
    global a
    global cnt

    if '(' not in a and a:
        while a:
            cnt += 1
            a.pop(0)
        return cnt

    while a[-1] == ')':
        a.pop()

    while a[-1] != '(':
        a.pop()
        cnt += 1

    a.pop()
    cnt = int(a.pop()) * cnt

    while a and a[-1] != ')' and a[-1] != '(':
        a.pop()
        cnt += 1

    if not a:
        return cnt

    return com()


a = list(input())
cnt = 0
print(com())