from collections import deque

def bfs(x,y):
    q= deque()
    q.append((x,y))
    dx = [0,0,-1,1,1,-1,1,-1]
    dy = [1,-1,0,0,1,-1,-1,1]
    while(q):
        x,y = q.popleft()
        for i in range(8):
            nx = x+ dx[i]
            ny = y+ dy[i]
            if 0<=nx<h and 0<=ny<w:
                if graph[nx][ny] ==1 and visited[nx][ny] ==False:
                    visited[nx][ny] =True
                    q.append((nx,ny))

answer = []

while(1):
    w,h = map(int,input().split())
    if w==0 and h==0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    visited = [[False]*w for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] ==1 and visited[i][j] == False:
                bfs(i,j)
                ans+=1
    answer.append(ans)

for i in answer:
    print(i)
