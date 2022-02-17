import sys, heapq

tc = int(sys.stdin.readline())
right_min_heap =[]
left_max_heap =[]
for _ in range(tc):
    num = int(sys.stdin.readline())
    if _ ==0:
        median = num
        heapq.heappush(left_max_heap, (-num, num))
    else:
        if num >= median:
            heapq.heappush(right_min_heap,(num,num))
        else:
            heapq.heappush(left_max_heap,(-num,num))

        if len(right_min_heap)-len(left_max_heap) >=1:
            x= heapq.heappop(right_min_heap)[1]
            heapq.heappush(left_max_heap,(-x,x))
        elif len(left_max_heap)-len(right_min_heap)>1:
            y =heapq.heappop(left_max_heap)[1]
            heapq.heappush(right_min_heap,(y,y))
        median = left_max_heap[0][1]
    # print('right_min_heap :',right_min_heap)
    # print('left_max_heap :',left_max_heap)
    print(median)