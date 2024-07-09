import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split(' '))

dx, dy = [0,0,-1,1], [-1,1,0,0]


#graph
graph = [list(map(int, input().split(' '))) for _ in range(n)]


#visited
visited = [[-1]*m for _ in range(n)]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    visited[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            n_x, n_y = dx[i] + x, dy[i] + y

            if 0 <= n_x < n and 0 <= n_y < m and visited[n_x][n_y] == -1:
                if graph[n_x][n_y] == 0:
                    visited[n_x][n_y] = 0
                elif graph[n_x][n_y] == 1:
                    visited[n_x][n_y] = visited[x][y] +1
                    queue.append((n_x, n_y))


for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and visited[i][j] == -1:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else: 
            print(visited[i][j], end=' ')
    print()




