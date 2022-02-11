case = int(input())
for i in range(0,case):
    a, b = map(int,input().split())
    n = b - a
    rule = 0
    i = 1
    count = 1
    while rule <n:
        rule += 2*i
        i +=1
    if rule - n >= (i-1):
        answer = ((i-1)*2) -1
    else:
        answer = (i-1) *2
    print(answer)