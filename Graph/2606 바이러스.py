n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start):
    visited[start]=1
    for i in graph[start]:
        if visited[i] ==0:
            dfs(i)

dfs(1)
answer=0
for i in visited[2:]:
    if i==1:
        answer+=1
print(answer)
