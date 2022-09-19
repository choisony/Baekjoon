n,m = map(int,input().split())
d = list(map(int,input().split()))
d.sort(reverse = True)
print(d[m-1])
