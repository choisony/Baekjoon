from collections import deque

n,m = map(int,input().split())
num_list = list(map(int,input().split()))
num_deq = deque(num_list)

deq= deque([i for i in range(1,n+1)])

#### 2 3 4 5 6 7 8 9 10
####
####
####
####
####
####


count =0
for i in num_list:
    count_left=0
    count_right =0

    if deq[0] == i:
        num_deq.popleft()
        deq.popleft()
    else:
        while(deq[0] != i):
            deq.rotate(-1)
            count_right+=1
        deq.rotate(count_right)
        while(deq[0] !=i):
            deq.rotate(1)
            count_left +=1
        deq.rotate(-count_left)

        if count_right<=count_left:
            deq.rotate(-count_right)
            count +=count_right
        else:
            deq.rotate(count_left)
            count +=count_left
    if len(deq)>0 and deq[0] == i:
        num_deq.popleft()
        deq.popleft()
print(count)