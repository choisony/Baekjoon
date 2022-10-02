import sys
from collections import deque

nx = [0,1,0,-1]
ny = [1,0,-1,0]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<n) and (0<=ny<m):
                if d[nx][ny] !=0 and visited[nx][ny]==99999:
                    q.append((nx,ny))
                    visited[nx][ny] = min(visited[nx][ny],visited[x][y]+1)




n,m = map(int,sys.stdin.readline().split())
d=[]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(n):
    temp =[]
    line = input()
    for j in line:
        temp.append(int(j))
    d.append(temp)
visited = [[99999]*m for i in range(n)]
visited[0][0]= 1
bfs(0,0)
print(visited[n-1][m-1])
