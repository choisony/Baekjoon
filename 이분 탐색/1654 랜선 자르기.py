k,n = map(int,input().split())
line = []
for _ in range(k):
    line.append(int(input()))

left = 1
right = max(line)
mid_temp=[]
while(left<=right):
    mid = (left + right) // 2
    ans = 0
    for i in line:
        ans += i//mid
    if ans >=n:
        left = mid+1
    else:
        right = mid-1

print(right)
