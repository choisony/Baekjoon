h = []
for i in range(9):
    h.append(int(input()))
save=[0]*2
sum_h = sum(h)
for a in range(len(h)):
    for b in range(a+1,len(h)):
        if sum_h-(h[a]+h[b])==100:
            save[0]=h[a]
            save[1]=h[b]
h.remove(save[0])
h.remove(save[1])

h.sort()
for i in h:
    print(i)
