import heapq
import sys
n, e = map(int,sys.stdin.readline().split())
start = int(input())
# graph=
graph =  [[] for _ in range(n+1)]

for _ in range(e):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))

max_num = float('inf')
dist= [max_num]* (n+1)
visited = [False] * (n+1)

dist[start] = 0
def go(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        weight, next=  heapq.heappop(q)
        if dist[next] < weight:
            continue
        if visited[next] ==False:
            visited[next] = True
            for next2,weight2 in graph[next]:
                cost = dist[next]+weight2
                if dist[next2] > cost:
                    dist[next2] = cost
                    heapq.heappush(q,(cost,next2))


go(start)
for i in dist[1:]:
    if i == max_num:
        print("INF")
    else:
        print(i)
