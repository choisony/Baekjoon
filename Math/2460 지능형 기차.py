answer= 0
temp=0
for i in range(10):
    comeout, comein = map(int,input().split())
    temp+= comein-comeout
    answer = max(temp,answer)
print(answer)
