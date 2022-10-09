n= int(input())
d=[]
for i in range(n):
    d.append(list(map(int,input().split())))
d.sort(key = lambda x: (x[1],x[0]))
time = 0
ans=0
for i in d:
    if i[0]>=time:
        time = i[1]
        # print(i[0],i[1])
        ans+=1
print(ans)
