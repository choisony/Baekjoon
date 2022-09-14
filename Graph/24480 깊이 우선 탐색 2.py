import sys
sys.setrecursionlimit(10**9)

def dfs(start):
    global count
    visited[start] = count
    for i in graph[start]:
        if visited[i]==0:
            count+=1
            dfs(i)

n,m,r = map(int,sys.stdin.readline().split())
visited = [0]*(n+1)
graph =[[] for i in range(n+1)]
count =1

for _ in range(m):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    if i:
        i.sort(reverse=True)


dfs(r)
for i in visited[1:]:
    print(i)
