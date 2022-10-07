def possible(x):
    for i in range(x):
        if chess[x]==chess[i] or abs(x-i)==abs(chess[x]-chess[i]):
            return False
    return True

def n_queens(i):
    global answer
    if i==n:
        answer+=1
        return
    else:
        for k in range(n):
            chess[i] = k
            if possible(i) ==1:
                n_queens(i+1)


n= int(input())


answer= 0
chess=[0]*n
n_queens(0)
print(answer)
