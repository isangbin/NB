import sys
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
idx = [_ for _ in range(N)]

tmp = list(zip(nums, idx))

stack = []
top = -1
ans = [0] * N

for i in range(N):
    # stack이 비었으면 무지성 push
    if stack == []:
        stack.append(tmp[i])
        top += 1

    # stack이 안비었으면
    else:
        while True:
            if stack != [] and tmp[i][0] > stack[top][0]:
                dump = stack.pop(-1)
                top -= 1
                ans[dump[1]] = tmp[i][0]
            else:
                break
        stack.append(tmp[i])
        top += 1

for i in stack:
    ans[i[1]] = -1

print(*ans)