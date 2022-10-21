from collections import deque
import copy
tc = int(input())
for _ in range(tc):
    func = input()
    n = int(input())
    num_list =input()
    num_list = num_list.replace('[','').replace(']','').replace(","," ")
    if n>=1:
        num_list = list(map(int,num_list.split()))
    else:
        num_list = []

    num_list = deque(num_list)
    rotate_num_list = copy.deepcopy(num_list)
    rotate_num_list.reverse()

    r=0
    error_temp = False
    for i in func:
        if i =="R":
            r+=1
        if i =="D":
            if len(num_list)>0:
                if r%2 ==0:
                    num_list.popleft()
                    rotate_num_list.pop()
                else:
                    num_list.pop()
                    rotate_num_list.popleft()
            else:
                error_temp = True
                break

    if error_temp==True:
        print("error",end="")
    else:
        if len(num_list) ==0:
            print("[]",end="")
        else:
            if r%2==0:
                print("[",end ="")
                for i in range(len(num_list)-1):
                    print(num_list[i],end=",")
                print(num_list[-1],end="]")
            else:
                print("[", end="")
                for i in range(len(rotate_num_list) - 1):
                    print(rotate_num_list[i], end=",")
                print(rotate_num_list[-1], end="]")
    print()


