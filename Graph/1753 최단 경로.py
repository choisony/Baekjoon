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


################# Priority Queue 시간초과 #################
# from queue import PriorityQueue
# import sys
# n,e = map(int,sys.stdin.readline().split())
# start = int(input())
# graph2 = {} # 딕셔너리로 {1: [[1,1],[2,3]] } 이런식으로 가중치 있는거만 골라야함
# for i in range(1,n+1):
#     graph2[i] = {}
# for _ in range(e):
#     u,v,w = map(int,sys.stdin.readline().split())
#
#     if v in graph2[u]:
#         graph2[u][v] = min(graph2[u][v],w)
#     else:
#         graph2[u][v] = w
#
# max_num = float('inf')
# dist= [max_num]* (n+1)
# visited = [False] * (n+1)
# dist[start] = 0
# q = PriorityQueue()
# q.put([0, start])
# def go(start):
#     while not q.empty():
#         weight, next= q.get()
#         if dist[next] < weight:
#             continue
#         if visited[next] ==False:
#             visited[next] = True
#             if graph2[next]:
#                 for next2,weight2 in graph2[next].items():
#                     cost = dist[next]+weight2
#                     if dist[next2] > cost:
#                         dist[next2] = cost
#                         if visited[next2]==False:
#                             q.put([cost,next2])
#
# go(start)
#
# for i in dist[1:]:
#     if i == max_num:
#         print("INF")
#     else:
#         print(i)



