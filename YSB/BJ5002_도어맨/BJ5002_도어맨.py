import sys
sys.stdin = open('input.txt', 'r')

X = int(input())
p = list(sys.stdin.readline())
club = []
m = 0
w = 0

while len(p) > 0:

    if len(p) >= 2 and m-w == X and p[0] == 'M':
        if p[1] == 'W':
            p.pop(1)
            w += 1

        else:
            break

    elif len(p) >= 2 and w-m == X and p[0] == 'W':
        if p[1] == 'M':
            p.pop(1)
            m += 1

        else:
            break

    else:
        tmp = p.pop(0)
        if tmp == 'M':
            m += 1

        else:
            w += 1


ans = m + w
print(ans)