n = int(input())
nl = list(map(int,input().split()))

che = [True] * 1001 #소수면 True
che[1] = False
for i in range(2,501):
    for j in range(2*i,1001,i):
        che[j] = False
cnt = 0        
for i in nl:
    if che[i] == True:
        cnt+=1
print(cnt)
