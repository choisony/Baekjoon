n,m = map(int,input().split())
block = list(map(int,input().split()))
ans = 0
for i in range(1,len(block)-1):
    left_max = max(block[:i])
    right_max = max(block[i+1:])

    height = min(left_max,right_max)
    if block[i] < height:
        ans += height - block[i]
print(ans)


https://www.acmicpc.net/problem/14719
