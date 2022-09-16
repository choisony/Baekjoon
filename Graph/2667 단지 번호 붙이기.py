def dfs(x,y):
    global count_n
    if (x>=0 and x<n) and (y>=0 and y<n):
        if d[x][y] == 1:
            d[x][y]= 0
            count_n+=1
            for i in range(4):
                dfs(x+nx[i],y+ny[i])

n = int(input())
d= []
for i in range(n):
    line = input()
    temp=[]
    for j in line:
        temp.append(int(j))
    d.append(temp)

nx = [0,0,1,-1]
ny = [1,-1,0,0]
city_count = 0
answer=[]
for i in range(n):
    for j in range(n):
        count_n=0
        if d[i][j] ==1:
            dfs(i,j)
            city_count+=1
            answer.append(count_n)
print(city_count)
answer.sort()
for x in answer:
    print(x)
