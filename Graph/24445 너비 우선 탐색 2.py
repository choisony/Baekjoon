import sys
from collections import deque

sys.setrecursionlimit(10 ** 9)


def bfs(r):
    global count
    visited[r] = count
    q.append(r)
    while (q):
        next = q.popleft()
        for i in graph[next]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                q.append(i)


n, m, r = map(int, sys.stdin.readline().split())
visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
count = 1

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)
q = deque()
bfs(r)

for i in visited[1:]:
    print(i)
