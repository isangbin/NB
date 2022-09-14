# BOJ_11053 가장 긴 증가하는 부분 수열
# 2022-09-11

# 숫자 개수, 숫자 입력
N = int(input())
numbers = list(map(int, input().split()))


# 증가하는 수열의 최소 값은 1 이므로
# 숫자 개수 만큼 1로 초기화
cnt_stack = [1] * N

# 2번째 인덱스부터 끝까지 순회 하며
for i in range(1, N):
    # 현재 인덱스 이전까지 순회해
    for j in range(i):
        # 현재 인덱스가 이전 인덱스의 숫자 보다 클 때
        if numbers[j] < numbers[i]:
            # 이전 인덱스에 저장된 증가하는 숫자에 1개 더한 것이
            # 현재 인덱스에 저장된 증가하는 숫자 개수 보다 크면
            if cnt_stack[j] + 1 > cnt_stack[i]:
                # 현재 저장된 증가하는 숫자 개수에 1을 더해 저장
                cnt_stack[i] = cnt_stack[j] + 1

# stack에 저장된 값 중 최대값을 출력
print(max(cnt_stack))


