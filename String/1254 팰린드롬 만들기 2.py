s= list(input())
idx= 0
while(s!=s[::-1] and idx<len(s)):
    s.insert(len(s)-idx,s[idx])
    idx+=1

print(len(s))
