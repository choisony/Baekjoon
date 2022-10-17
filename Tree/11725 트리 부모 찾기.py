from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [0]*(n+1)

def bfs(a):
    global parent
    q=deque()
    q.append(a)
    while(q):
        x = q.popleft()
        for i in graph[x]:
            if parent[i] ==0 and i !=1:
                parent[i] = x
                q.append(i)

bfs(1)
for i in range(2,n+1):
    print(parent[i],end=' ')
