import sys
from collections import deque
sys.setrecursionlimit(10000) 

T = int(sys.stdin.readline())

dx, dy = [0,0,-1,1], [-1,1,0,0]


def dfs(x,y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    
    if map_list[x][y] == 1:
        map_list[x][y] =0
    
        for i in range(4):
            n_x,  n_y = x + dx[i], y + dy[i]
            dfs(n_x, n_y)

        return True

    return False
    

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    map_list = [[0]* M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        map_list[y][x] = 1


    cnt = 0

    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                cnt += 1
    print(cnt)
