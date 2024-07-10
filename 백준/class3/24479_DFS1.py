import sys

def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

sys.setrecursionlimit(150000)

N, M, R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 1

for i in range(M):
    edge1, edge2 = map(int, sys.stdin.readline().split())
    line[edge1].append(edge2)
    line[edge2].append(edge1)



dfs(R)

for output in range(1, N+1):
    print(visited[output])





