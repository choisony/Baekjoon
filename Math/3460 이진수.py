tc = int(input())
for i in range(tc):
    n = int(input())

    op_nbin = bin(n)[::-1]

    for i in range(len(op_nbin)):
        if op_nbin[i]=="1":
            print(i,end=" ")
