from collections import deque
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(input()))

visited = [[0]*len(graph[0]) for i in range(n)]

def bfs(x,y):
    global color
    q= deque()
    q.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<len(graph[0]):
                if graph[nx][ny] == color and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    q.append((nx,ny))

def bfs_rg(x,y):
    global color
    q= deque()
    q.append((x,y))
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<len(graph[0]):
                if color =="G":
                    if (graph[nx][ny] == "R" or graph[nx][ny] == "G") and visited_RG[nx][ny]==0:
                        visited_RG[nx][ny] = 1
                        q.append((nx,ny))
                if color == "R":
                    if (graph[nx][ny] == "G" or graph[nx][ny] == "R") and visited_RG[nx][ny] == 0:
                        visited_RG[nx][ny] = 1
                        q.append((nx, ny))
                if color =="B":
                    if graph[nx][ny] == "B" and visited_RG[nx][ny] == 0:
                        visited_RG[nx][ny] = 1
                        q.append((nx, ny))
ans = 0
for i in range(n):
    for j in range(len(graph[0])):
        if visited[i][j] ==0:
            color = graph[i][j]
            bfs(i,j)
            ans+=1

ans_RG = 0
visited_RG =[[0]*len(graph[0]) for i in range(n)]

for i in range(n):
    for j in range(len(graph[0])):
        if visited_RG[i][j] ==0:
            color = graph[i][j]
            bfs_rg(i,j)
            ans_RG+=1

print(ans, ans_RG)

