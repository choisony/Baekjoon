from collections import deque
import copy
def bfs():
    q = deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                q.append((i,j))
    while(q):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<m:
                if tmp_graph[nx][ny] ==0:
                    tmp_graph[nx][ny] = 2
                    q.append((nx,ny))
    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer = max(cnt,answer)
    print(tmp_graph)

def make_wall(cnt):
    if cnt==3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0:
                graph[i][j] = 1
                make_wall(cnt+1)
                graph[i][j]=0


n,m = map(int,input().split())
graph =[]
dx= [0,0,1,-1]
dy= [1,-1,0,0]
for i in range(n):
    xx = list(map(int,input().split()))
    graph.append(xx)

answer=0
make_wall(0)
print(answer)
