import sys
sys.setrecursionlimit(10**9)

def dfs(x,y):
    if x>=0 and x<n and y>=0 and y<m:
        if d[x][y] == 1:
            d[x][y] = 0
            for f in range(4):
                dfs(x+nx[f],y+ny[f])

tc = int(input())
nx=[0,0,1,-1]
ny=[1,-1,0,0]
for case in range(tc):
    answer= 0
    m, n, k = map(int, input().split())
    d = [[0]*m for i in range(n)]
    for _ in range(k):
        x,y = map(int,input().split())
        d[y][x] =1
    for i in range(n):
        for j in range(m):
            if d[i][j]==1:
                dfs(i,j)
                answer+=1
    print(answer)
