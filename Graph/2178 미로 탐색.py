import sys
sys.setrecursionlimit(10**9)

nx = [0,1,0,-1]
ny = [1,0,-1,0]

def dfs(x,y):
    if x>=0 and x<n and y>=0 and y<m:
        if d[x][y] == 1 :
            for i in range(4):
                if x+nx[i]>=0 and x+nx[i]<n and y+ny[i]>=0 and y+ny[i]<m and d[x+nx[i]][y+ny[i]]==1:
                    if visited[x][y]+1 < visited[x+nx[i]][y+ny[i]]:
                        visited[x+nx[i]][y+ny[i]] = visited[x][y]+1
                        dfs(x+nx[i],y+ny[i])




n,m = map(int,sys.stdin.readline().split())
d=[]
for i in range(n):
    temp =[]
    line = input()
    for j in line:
        temp.append(int(j))
    d.append(temp)
visited = [[99999]*m for i in range(n)]
visited[0][0]= 1
dfs(0,0)
print(visited[n-1][m-1])
