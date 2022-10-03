n,k = map(int,input().split())
d=[]
for i in range(1,n//2+1):
    if n%i==0:
        d.append(i)
d.append(n)

if len(d)<k:
    print("0")
else:
    print(d[k-1])
