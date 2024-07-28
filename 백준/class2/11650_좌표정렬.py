import sys

# 정렬 key를 x, y 순으로 주면 됨, 들어오는 좌표값들을 튜플로 받고 정렬

N = int(sys.stdin.readline())
arr = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    arr.append((x,y))

sorted_list = sorted(arr, key = lambda x: (x[0], x[1]))

for i in sorted_list:
    print(i[0], i[1])
