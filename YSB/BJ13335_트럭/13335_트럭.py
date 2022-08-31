import sys
sys.stdin = open('input.txt', 'r')

# n: 트럭 수 / w: 다리 길이 / L: 최대 하중
n, w, L = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))

bridge = [0] * w
weight = 0
cnt = 0

# 마지막 트럭이 다리에 올라갈 때 까지 실행
while len(truck) != 0:
    if weight + truck[0] - bridge[0] <= L:   # 올라가도 무게초과 아닐 시
        bridge.append(truck.pop(0))
        weight = weight + bridge[-1] - bridge.pop(0)
        cnt += 1
        print(bridge, truck)
    else:   # 올라가면 무게초과일 시
        bridge.append(0)
        weight -= bridge.pop(0)
        cnt += 1
        print(bridge, truck)


# 마지막 트럭이 다리를 통과해야하므로 w 더해줌
cnt += w
print(cnt)