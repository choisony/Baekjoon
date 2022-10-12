import copy
from collections import deque

def bfs(cnt):

    dx= [0,0,1,-1]
    dy= [1,-1,0,0]
    while(q):
        cnt,x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0<=nx<m and 0<=ny<n) and graph[nx][ny] ==0:
                graph[nx][ny] = 1
                q.append((cnt+1,nx,ny))
    return cnt


n,m = map(int,input().split())
graph = []
for i in range(m):
    graph.append(list(map(int,input().split())))

q = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            q.append((0,i,j))


ans = bfs(0)
cnt= 0
for i in graph:
    cnt += i.count(0)

print(-1 if cnt else ans)
