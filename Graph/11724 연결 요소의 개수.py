import sys
sys.setrecursionlimit(10**9)
from collections import deque
# def dfs(x):
#     visited[x]=1
#     for i in graph[x]:
#         if visited[i] ==0:
#             dfs(i)

def bfs(x):
    q=deque()
    q.append(x)
    visited[x]=1
    while(q):
        next = q.popleft()
        for i in graph[next]:
            if visited[i] ==0:
                visited[i] = 1
                q.append(i)



n,m = map(int,sys.stdin.readline().split())
visited= [0]*(n+1)
graph = [[] for i in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0

for i in range(1,n+1):
    if visited[i] ==0:
        # dfs(i)
        bfs(i)
        ans+=1

print(ans)
