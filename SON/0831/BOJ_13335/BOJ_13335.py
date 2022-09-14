# BOJ_13335 트럭
# 2022-08-27

n, w, L = map(int, input().split())
a = list(map(int, input().split()))

# 다리 길이 만큼 표현하기 위해 0으로 초기화
stack = [0 for i in range(w)]
time = 0
while True:
    # 다리(stack)에 올라가 있는 무게와 현재 트럭 무게 합이 최대 하중보다 작으면
    # 최대로 트럭이 올라 갔을 때까지
    while a and sum(stack) + a[0] <= L:
        # 트럭 한칸씩 앞으로 움직 이고 시간 1 추가
        stack.pop(0)
        stack.append(a.pop(0))
        time += 1
    # 트럭이 다리 끝 도착할 떄 까지 앞에 0 빼고 뒤에 붙이기
    while stack[0] == 0:
        stack.append(stack.pop(0))
        time += 1

    # 트럭이 끝에 도착 하면 빼고
    stack.pop(0)
    # 다리에 트럭이 더 들어갈 수 있으면 트럭 집어 넣고
    if a and sum(stack) + a[0] <= L:
        stack.append(a.pop(0))
        time += 1
    # 더 못들어가면 0 넣기
    else:
        stack.append(0)
        time += 1

    # 더 이상 들어갈 트럭이 없고 다리 위에도 없으면 탈출
    if not a and not sum(stack):
        break

print(time)