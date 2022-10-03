a,b = map(int,input().split())

d=[]
idx = 0
while(len(d)<1000):
    idx +=1
    for i in range(idx):
        d.append(idx)
print(sum(d[a-1:b]))
