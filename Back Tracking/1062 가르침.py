from collections import Counter
n, k = map(int,input().split())
if k<5:
    print(0)
    exit()
if k==26:
    print(n)
    exit()
words= []
for i in range(n):
    words.append(set(input()[4:-4]))


bit = [0]*26
d = ['a','n','t','c','i']
for i in d:
    bit[ord(i)-ord('a')]= 1

answer = 0
def dfs(idx,cnt):
    global answer
    if cnt == k-5:
        wc= 0
        for word in words:
            temp = True
            for j in word:
                if bit[ord(j)-ord('a')] == 0:
                    temp = False
                    break
            if temp == True:
                wc+=1
        answer= max(wc,answer)
        return

    for i in range(idx,26):
        if bit[i] ==0:
            bit[i] = 1
            dfs(i+1,cnt+1)
            bit[i] = 0

dfs(0,0)
print(answer)
