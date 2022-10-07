import sys
n,m = map(int,sys.stdin.readline().split())
listen=set()
for _ in range(n):
    listen.add(input())
see=set()
for _ in range(m):
    see.add(input())


ans = listen & see
ans= sorted(ans)
print(len(ans))
for i in ans:
    print(i)
