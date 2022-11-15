def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])

def union(u, v):
    u = find(u)
    v = find(v)
    if u < v:
        parent[v] = u
    if v < u:
        parent[u] = v

n = int(input())
m = int(input())
graph = []
for _ in range(n):
    temp = list(map(int,input().split()))
    graph.append(temp)

route = list(map(int,input().split()))
for i in range(len(route)):
    route[i] -=1

parent = [i for i in range(n)]

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == 1:
            union(i,j)

parent_first = find(route[0])

answer=True
for i in route:
    if parent_first != find(i):
        answer=False
        break

print("NO") if answer==False else print("YES")
