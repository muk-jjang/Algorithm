import sys

N = int(input())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

result = 0 
for i in range(N):
    if A[i] <= B[i]:
        result += 1

print(result)