import sys

N = int(sys.stdin.readline())


def preorder(n):
    if n:
        print(alpha[n], end='')
        preorder(ch1[n])
        preorder(ch2[n])

def inorder(n):
    if n:
        inorder(ch1[n])
        print(alpha[n], end='')
        inorder(ch2[n])

def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(alpha[n], end='')


ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
alpha = ['.', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(N):
    x, y, z = map(str, sys.stdin.readline().split())
    x = alpha.index(x)
    y = alpha.index(y)
    z = alpha.index(z)
    ch1[x] = y
    ch2[x] = z

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()


