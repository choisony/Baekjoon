from collections import deque

n, e = map(int,input().split())
start = int(input())
# graph=  [[0]* (n+1) for i in range(n+1)] # 이거로 풀면 메모리 초과
graph2 = {} # 딕셔너리로 {1: [[1,1],[2,3]] } 이런식으로 가중치 있는거만 골라야함
for _ in range(e):
    u,v,w = map(int,input().split())
    # graph[u][v] = w
    if u in graph2:
        graph2[u].append([v,w])
    else:
        graph2[u] = [[v,w]]


visited= [99999999]* (n+1)

visited[1] = 0
def go(start):
    q = deque()
    q.append((start,0))
    while(q):
        next, weight= q.popleft()
        if visited[next] < weight:
            continue
        # for i in range(len(graph[next])):
        #     if graph[next][i] !=0:
        #         next2, weight2 = i,graph[next][i]
        #         if visited[next2] > visited[next]+weight2:
        #             visited[next2] = visited[next]+weight2
        #             q.append(next2)
        if next in graph2:
            for i in graph2[next]:
                next2, weight2 = i[0], i[1]
                if visited[next2] > visited[next]+weight2:
                    visited[next2] = visited[next]+weight2
                    q.append((next2,weight2))

go(1)
for i in visited[1:]:
    if i == 99999999:
        print("INF")
    else:
        print(i)
