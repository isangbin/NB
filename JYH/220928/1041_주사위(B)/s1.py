# 1041_주사위(B)
# 2022-09-26

import sys 
sys.stdin = open('input.txt', 'r')

N = int(sys.stdin.readline()) 
arr = list(map(int, sys.stdin.readline().split())) # 리스트로 받으니 런타임에러에서 통과함..

square3 = 4 # 3면이 보이는 개수
square2 = 4*(N-1) + 4*(N-2) # 2면
square1 = 4*(N-1)*(N-2) + (N-2)*(N-2) # 1면

value = [min(arr[0], arr[5]), min(arr[1], arr[4]), min(arr[2], arr[3])] # 마주보는 면 중에서 더 작은 값 채택
value.sort() # 작은 값부터 정렬

if N == 1: # N이 1일 때 따로 생각해줘야 함
    print(sum(arr) - max(arr))
else:
    print(square3 * sum(value[0:3]) + square2 * sum(value[0:2]) + square1 * value[0])
