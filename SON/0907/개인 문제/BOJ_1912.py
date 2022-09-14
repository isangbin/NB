# BOJ_1912 연속합 문제풀이
# 2022-09-04

N = int(input())

# 입력값
num_list = list(map(int, input().split()))

# 숫자 값 중 맨 처음 값으로 sum_list 초기화
sum_list = [num_list[0]]

# index 1부터 끝까지 돌면서
for i in range(1, N):
    # 이전 까지의 합이 0보다 크거나 같을 때만 (음수이면 오히려 숫자가 감소하므로)
    if sum_list[i-1] >= 0:
        # 합 리스트에 이전까지의 합에 현재 숫자 더하기
        sum_list.append(sum_list[i-1] + num_list[i])
    # 이전 까지의 합이 0보다 작으면 현재 값을 현재까지의 합으로 초기화
    else:
        sum_list.append(num_list[i])

# 앞에서 부터 양수일 때만 더했던 값들 중 최대값 출력
print(max(sum_list))