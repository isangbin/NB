# 1991_트리 순회(B)
# 2022-09-16

import sys
sys.stdin = open('input.txt', 'r')

def preorder(n):
    if n:
        print(chr(n+64), end='')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(chr(n+64), end='')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n+64), end='')


N = int(sys.stdin.readline())
# 부모를 인덱스로 하여 자식 리스트(2개) 만들기
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    ord_node = ord(node)-64
    if left == '.' and right == '.':
        pass
    elif left == '.':
        ch2[ord_node] = ord(right)-64
    elif right == '.':
        ch1[ord_node] = ord(left)-64
    else: 
        ch1[ord_node] = ord(left)-64
        ch2[ord_node] = ord(right)-64

# 순회
preorder(1)
print()
inorder(1)
print()
postorder(1)