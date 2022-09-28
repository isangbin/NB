# BOJ_1662 문제풀이
# 2022-08-27

def com():
    global number
    global a

    if '(' not in a:
        return a
    while a[-1] == ')':
        a.pop()
    while a[-1] != '(':
        number = a.pop() + number
    a.pop()
    number = int(a.pop()) * number

    while a and a[-1] != ')' and a[-1] != '(':
        number = a.pop() + number
        if not a:
            return number
    return com()


a = list(input())
number = ''
print(len(com()))