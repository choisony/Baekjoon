def dfs(start):
    dfs_answer.append(start)
    global count
    visited[start] = count
    for i in graph[start]:
        if visited[i] ==0:
            count +=1
            dfs(i)

def bfs(start):
    bfs_answer.append(start)
    global count
    q.append(start)
    visited[start] = count
    while(q):
        next= q.popleft()
        for i in graph[next]:
            if visited[i] == 0:
                q.append(i)
                count+=1
                visited[i] = count
                bfs_answer.append(i)

import sys
from collections import deque
dfs_answer=[]
bfs_answer=[]
n,m,start = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
count = 1

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    i.sort()


dfs(start)
for i in dfs_answer:
    print(i,end= " ")
print()
visited = [0]*(n+1)
count = 1
q= deque()
bfs(start)
for i in bfs_answer:
    print(i,end= " ")
