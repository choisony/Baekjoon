import heapq

tc = int(input())
for _ in range(tc):
    n = int(input())
    num = list(map(int,input().split()))
    num.sort()
    h=[]
    for i in num:
        heapq.heappush(h,i)
    ans = 0
    while(len(h)>=2):
        x=heapq.heappop(h)
        y=heapq.heappop(h)
        ans += (x+y)
        heapq.heappush(h,x+y)
    print(ans)
