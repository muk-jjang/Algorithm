import sys

'''접근방법
N이 1에서 100000, 그리고 시간 제한은 0.5초
1초에 2000만번 연산하는 것을 생각하면 구간마다 매번 구하면 해결 불가능
따라서 구간합 arr을 만들어 놓고 해당 부분에서 바로 탐색할 수 있도록 구성
'''

N, M  = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

prefix_list = [0]
sum = 0

# 구간합
for i in arr:
    sum += i
    prefix_list.append(sum)

# 출력
for i in range(M):
    start, end = map(int, sys.stdin.readline().split())

    print(prefix_list[end] - prefix_list[start-1])

