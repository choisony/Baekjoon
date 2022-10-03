n = int(input())
m = int(input())

che = [True] * (m+1) #소수면 True
che[1] = False
for i in range(2,(m//2)+1):
    for j in range(2*i,m+1,i):
        che[j] = False

ans =[]
for j in range(n,m+1):
    if che[j] == True:
       ans.append(j)
        
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)
