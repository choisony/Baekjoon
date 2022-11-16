from collections import deque

N = int(input()) # n*n square
k = int(input()) # apple
graph = [[0]*N for _ in range(N)]
where = "RIGHT"
for _ in range(k):
    x,y = map(int,input().split())
    graph[x-1][y-1] = 1

L =  int(input())
change = {}
for _ in range(L):
    sec, direction = map(str,input().split())
    sec = int(sec)
    change[sec] = direction

idx = 0
q = deque()
q.append((0,0))
while(q):
    x, y = q[-1][0], q[-1][1]
    if 0<=x<N and 0<=y<N:
        if idx in change:
            if change[idx] == "L":
                if where == "RIGHT":
                    where = "UP"
                elif where == "UP":
                    where = "LEFT"
                elif where == "LEFT":
                    where = "DOWN"
                elif where == "DOWN":
                    where = "RIGHT"
            if change[idx] == "D":
                if where == "RIGHT":
                    where = "DOWN"
                elif where == "DOWN":
                    where = "LEFT"
                elif where == "LEFT":
                    where = "UP"
                elif where == "UP":
                    where = "RIGHT"
        if where == "RIGHT":
            if (x, y+1) in q:
                break
            q.append((x,y+1))
            if 0<=x<N and 0<=y+1<N:
                if graph[x][y+1] == 0:
                    q.popleft()
                else:
                    graph[x][y+1] = 0
            else:
                break
        elif where == "DOWN":
            if (x+1, y) in q:
                break
            q.append((x+1,y))
            if 0<=x+1<N and 0<=y<N:
                if graph[x+1][y] == 0:
                    q.popleft()
                else:
                    graph[x+1][y] = 0
            else:
                break
        elif where =="LEFT":
            if (x, y-1) in q:
                break
            q.append((x,y-1))
            if 0<=x<N and 0<=y-1<N:
                if graph[x][y-1] == 0:
                    q.popleft()
                else:
                    graph[x][y-1] =0
            else:
                break
        elif where == "UP":
            if (x-1, y) in q:
                break
            q.append((x-1,y))
            if 0<=x-1<N and 0<=y<N:
                if graph[x-1][y] == 0:
                    q.popleft()
                else:
                    graph[x-1][y] =0
            else:
                break
        idx +=1
    else:
        break
print(idx+1)
