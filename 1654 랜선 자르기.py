k, n = map(int,input().split())
kl = []
for i in range(k):
    num = int(input())
    kl.append(num)
start = 1
end = max(kl)
ans_list = []

def check(num):
    av= 0
    for i in kl:
        av += i//num
    return av

while(start<=end):
    mid = (start+end)//2
    av = check(mid)
    if av <n:
        end = mid-1
    else:
        start = mid+1
print(end)
