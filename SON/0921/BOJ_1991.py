# BOJ_1991 트리 순회 문제풀이
# 2022-09-20
def pre(n):                     # 전위
    if n != '.' and n:
        print(n, end='')
        pre(ch1[n])
        pre(ch2[n])


def order(n):                   # 중위
    if n != '.' and n:
        order(ch1[n])
        print(n, end='')
        order(ch2[n])


def post(n):                    # 후위
    if n != '.' and n:
        post(ch1[n])
        post(ch2[n])
        print(n, end='')


N = int(input())

ch1 = dict()                    # 노드 정보가 문자이므로 딕셔너리 활용
ch2 = dict()

for i in range(N):
    info = list(input().split())
    ch1[info[0]] = info[1]      # 자식 정보 입력
    ch2[info[0]] = info[2]

pre('A')
print()
order('A')
print()
post('A')
print()