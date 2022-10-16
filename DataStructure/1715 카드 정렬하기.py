from collections import deque

n = int(input())
q=deque()
d=[]
for _ in range(n):
    d.append(int(input()))
    d.sort()
q = deque(d)
temp = deque()
if n ==1:
    print(0)
    exit()
elif n==2:
    print(q[0]+q[1])
    exit()
else:
    ans=0
    while(q):
        if len(q)==1 and not temp:
            q.popleft()
            break
        if (len(temp)>0 and q and temp[0]<q[0]) or (temp and not q):
            z = temp.popleft()
            q.appendleft(z)
        x = q.popleft()

        if (len(temp)>0 and q and temp[0]<q[0]) or (temp and not q):
            z = temp.popleft()
            q.appendleft(z)
        y= q.popleft() if q else 0

        next = x+y
        ans += next
        temp.append(next)
        if temp and q and temp[0]>=q[-1]:
            z = temp.popleft()
            q.append(z)
        if temp and not q:
            z = temp.popleft()
            q.append(z)

print(ans)
