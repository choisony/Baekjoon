from collections import deque

n,k = map(int,input().split())
if n>k:
    print(n-k)
    exit(0)
if n==k:
    print(0)
    exit()
k_masking = [0] * (100001)


def bfs(n):
    q=deque()
    q.append(n)
    while(q):
        num = q.popleft()
        if num ==k:
            print(k_masking[k])
            break
        for x in (num+1,num-1,num*2):
            if 0<=x<=100000  and not k_masking[x]:
                q.append(x)
                k_masking[x] = k_masking[num]+1
bfs(n)
