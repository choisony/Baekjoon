n,s = map(int,input().split())
num = list(map(int,input().split()))

if sum(num)<s:
    print(0)
    exit()

end =0
interval_sum =0

answer = []

for i in range(0,n):
    while interval_sum < s and end < n:
        interval_sum += num[end]
        end+=1
    # print('i: ', i, 'interval_sum: ', interval_sum, 'end: ', end)
    if interval_sum>=s:
        answer.append(end-i)

    interval_sum -= num[i]

print(min(answer))
