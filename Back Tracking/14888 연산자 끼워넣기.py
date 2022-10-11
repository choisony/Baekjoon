import math
n = int(input())
num = list(map(int,input().split()))
cal = list(map(int,input().split()))

## cal[0] = '+'
## cal[1] = '-'
## cal[2] = '*'
## cal[3] = '/'
max_ans = -99999
min_ans = 99999
ans=0
def dfs(i,ans):
    global max_ans,min_ans,cal
    if i==n:
        max_ans  = max(max_ans,ans)
        min_ans = min(min_ans,ans)
    else:
        if cal[0]>0:
            cal[0] -=1
            dfs(i+1,ans+ num[i])
            cal[0] +=1
        if cal[1]>0:
            cal[1] -=1
            dfs(i+1,ans- num[i])
            cal[1] +=1
        if cal[2]>0:
            cal[2] -=1
            dfs(i+1,ans* num[i])
            cal[2] +=1
        if cal[3]>0:
            cal[3] -=1
            dfs(i+1,int(ans/ num[i]))
            cal[3] +=1

dfs(1,num[0])
print(max_ans)
print(min_ans)


# import math
# n=-8
# m=3
# print(int(n/m))
# print(int(n//m))
# print(n//m)
# print(math.floor(n/m))
