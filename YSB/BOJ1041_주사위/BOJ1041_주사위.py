import sys
input = sys.stdin.readline

N = int(input())
dice = list(map(int, input().split()))

# 한 면만 보이는 개수
reveal1 = (N-2)*(N-1)*4 + (N-2)**2
# 두 면이 보이는 개수
reveal2 = (N-1)*4 + (N-2)*4
# 세 면이 보이는 개수
reveal3 = 4

min1 = min(dice)
min2 = float('inf')
min3 = float('inf')
for i in range(6):
    for j in range(6):
        if i == j or i + j == 5:
            pass
        else:
            min2 = min(min2, dice[i]+dice[j])

            for k in range(6):
                if k != i and k != j and k + i != 5 and k + j != 5:
                    min3 = min(min3, dice[i]+dice[j]+dice[k])

if N != 1:
    ans = min1*reveal1 + min2*reveal2 + min3*reveal3
else:
    ans = sum(dice) - max(dice)
print(ans)