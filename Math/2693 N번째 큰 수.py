tc = int(input())
for _ in range(tc):
    d = list(map(int,input().split()))
    d.sort(reverse=True)
    print(d[2])
